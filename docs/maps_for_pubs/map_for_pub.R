library(sf)
library(raster)
library(gridExtra)
library(tidyverse)
library(magick)

BIORE <- read.csv("maps_for_pubs/input/spec.dat") %>% 
    select(name) %>% 
    filter(grepl("BIORE_",name)) %>% 
    mutate(name=gsub("BIORE_","",name)) %>% 
    unlist() %>% 
    as.numeric()

proj <- "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +wktext  +no_defs"


bioregions <- st_read("maps_for_pubs/bioregion_short.shp",stringsAsFactors = FALSE) %>% 
    filter(BIOREGI %in% BIORE) %>% 
    mutate(BIOREGI=paste0("BIORE_",BIOREGI)) %>% 
    st_transform(proj)

pu <- read.csv("maps_for_pubs/output/pu_no_connect.csv") %>%
    mutate(geometry=st_as_sfc(geometry,"+proj=longlat +datum=WGS84"),
           best_solution = as.logical(best_solution)) %>%
    st_as_sf()%>% 
    st_transform(proj) %>% 
    select(pu_id)

# st_write(bioregions,"maps_for_pubs/bioregion_filtered.shp")

# intersection <- st_intersection(pu,bioregions)
# intersection$row <- 1:nrow(intersection)
# distances <- st_distance(intersection) %>% 
#     data.frame(check.names = FALSE) %>% 
#     mutate(row=row.names(.)) %>% 
#     gather(key="column",value="value",-row)
# 
# distances$row <- as.numeric(distances$row)
# distances$column <- as.numeric(distances$column)
# # con_list <- distances
# 
# con_list <- distances %>%
#     left_join(data.frame(intersection),by=c("row"="row")) %>% 
#     mutate(id1=as.numeric(pu_id),
#            from_BIO=BIOREGI) %>%
#     select(row,column,id1,from_BIO,value) %>% 
#     left_join(data.frame(intersection),by=c("column"="row")) %>% 
#     mutate(id2=as.numeric(pu_id),
#            to_BIO=BIOREGI) %>%
#     select(id1,from_BIO,id2,to_BIO,value) %>% 
#     filter(from_BIO==to_BIO,
#            as.numeric(value)>0) %>% 
#     mutate(habitat=to_BIO) %>% 
#     group_by(habitat,id1,id2) %>% 
#     summarize(value=1/mean(as.numeric(value))^2) %>% 
#     group_by(habitat,id1) %>% 
#     mutate(value=as.numeric(value)/sum(as.numeric(value)))
# 
# write.csv(con_list,"maps_for_pubs/IsolationByDistance.csv",quote=FALSE,row.names = FALSE)
# 
# con_list_mean <- con_list %>% 
#     group_by(id1,id2) %>% 
#     summarize(value=mean(value)) %>% 
#     mutate(habitat="mean") %>% 
#     as.data.frame() %>% 
#     complete(habitat,id1,id2,fill=list(value = 0)) %>% 
#     as.data.frame()
# 
# write.csv(con_list_mean,"maps_for_pubs/IsolationByDistance_mean.csv",quote=FALSE,row.names = FALSE)


# CF_landscape maps for publication


# set default projection for leaflet
proj <- "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +wktext  +no_defs"
proj_rotated <- "+proj=omerc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +wktext  +no_defs +alpha=-73.00000"

spec <- read.csv("maps_for_pubs/input/spec.dat")
puvspr <- read.csv("maps_for_pubs/input/puvspr2.dat")
pu <- read.csv("maps_for_pubs/input/pu.dat")

puvspr_wide <- puvspr %>%
    left_join(select(spec,"id","name"),
              by=c("species"="id")) %>%
    select(-species) %>%
    spread(key="name",value="amount")

# planning units with output
output <- read.csv("maps_for_pubs/output/pu_no_connect.csv") %>%
    mutate(geometry=st_as_sfc(geometry,"+proj=longlat +datum=WGS84"),
           best_solution = as.logical(best_solution)) %>%
    st_as_sf() %>%
    left_join(puvspr_wide,by=c("pu_id"="pu"))%>% 
    st_transform(proj)

output_rotated <- st_transform(output,proj_rotated)


output_connect <- read.csv("maps_for_pubs/output/pu_connect.csv") %>%
    mutate(geometry=st_as_sfc(geometry,"+proj=longlat +datum=WGS84"),
           best_solution = as.logical(best_solution)) %>%
    st_as_sf() %>%
    left_join(puvspr_wide,by=c("pu_id"="pu"))%>% 
    st_transform(proj) 

bioregions <- st_read("maps_for_pubs/bioregion_short.shp",stringsAsFactors = FALSE) %>% 
    st_transform(proj) %>% 
    mutate(BIOREGI=paste0("BIORE_",BIOREGI)) %>% 
    filter(BIOREGI %in% spec$name) %>% 
    group_by(BIOREGI,SHORT_D,ALT_LAB) %>% 
    summarize() %>% 
    data.frame() %>% 
    mutate(BIOREGI=as.character(BIOREGI),
           SHORT_D=unlist(lapply(lapply(strsplit(SHORT_D," "),tail,-1),paste,collapse=" "))) %>% 
    st_as_sf(crs=proj)

# bioregions[nrow(bioregions)+1,] <- st_as_sf(data.frame(BIOREGI="Planning Units",
# SHORT_D="Planning Units",
# geometry=st_combine(output)))
# bioregions$BIOREGI[nrow(bioregions)]="Planning Units"

# get basemap outline of AUS
bb <- output %>% 
    st_bbox() %>% 
    st_as_sfc() %>% 
    st_transform(proj) 

AUS <- getData(country="AUS",level=0) %>% 
    st_as_sf() %>% 
    st_transform(proj) %>% 
    st_intersection(st_buffer(bb,100000))


#### 3 panel #####

p1 <- ggplot(output_connect)+
    geom_sf(data=AUS,fill="grey",colour="darkgrey")+
    geom_sf(aes(fill=between_cent_land_pu_mean),colour="transparent",size=0.25)+
    scale_fill_distiller("Betweeness\nCentrality",palette="Oranges",direction = 1)+
    coord_sf(xlim=st_bbox(output_rotated)[c(1,3)],
             ylim=st_bbox(output_rotated)[c(2,4)],
             crs=proj_rotated,
             expand = FALSE)+
    theme_dark()+
    theme(legend.position = "bottom",
          legend.direction = "vertical",
          legend.background = element_rect(fill="transparent"),
          plot.title = element_text(size=10)) +
    ggtitle("A) Connect. Feature")

p2 <- ggplot(output)+
    geom_sf(data=AUS,fill="grey",colour="darkgrey")+
    geom_sf(aes(fill=select_freq),colour="transparent",size=0.25)+
    scale_fill_distiller("Selection\nFrequency",palette="Purples",direction = 1,limits=c(0,100))+
    coord_sf(xlim=st_bbox(output_rotated)[c(1,3)],
             ylim=st_bbox(output_rotated)[c(2,4)],
             crs=proj_rotated,
             expand = FALSE)+
    theme_dark()+
    theme(legend.position = "bottom",
          legend.direction = "vertical",
          legend.background = element_rect(fill="transparent"),
          plot.title = element_text(size=10))+
    ggtitle("B) Without Connectivity")


p3 <- ggplot(output_connect)+
    geom_sf(data=AUS,fill="grey",colour="darkgrey")+
    geom_sf(aes(fill=select_freq),colour="transparent",size=0.25)+
    scale_fill_distiller("Selection\nFrequency",palette="Purples",direction = 1,limits=c(0,100))+
    coord_sf(xlim=st_bbox(output_rotated)[c(1,3)],
             ylim=st_bbox(output_rotated)[c(2,4)],
             crs=proj_rotated,
             expand = FALSE)+
    theme_dark()+
    theme(legend.position = "bottom",
          legend.direction = "vertical",
          legend.background = element_rect(fill="transparent"),
          plot.title = element_text(size=10))+
    ggtitle("C) With Connectivity")


ggsave("maps_for_pubs/maps.png", grid.arrange(p1, p2, p3, ncol=3),width=7.25,height=8,dpi=600)

#### difference ####
output_connect$diff <- output_connect$select_freq-output$select_freq
output_connect$rep_select_freq <- output$select_freq

oc_greater90 <- output_connect %>% 
    filter(rep_select_freq>quantile(rep_select_freq,probs=0.9),
           select_freq>quantile(select_freq,probs=0.9))
oc_bottom5 <- output_connect %>% 
    filter(rep_select_freq<5,
           select_freq<5)
oc_sfcon <- output_connect %>% 
    filter(diff>5)
oc_sfrep <- output_connect %>% 
    filter(diff<(-5))

base <- ggplot(oc_sfrep)+
    geom_sf(data=AUS,fill="grey",colour="darkgrey")+
    geom_sf(aes(fill=diff),colour="transparent")+
    scale_fill_distiller("Selection frequency\nhigher without\nconnectivity",palette=c("Purples"),limits=c(-100,-5),
                         labels=c("100","75","50", "25", "5"))+
    coord_sf(xlim=st_bbox(output_rotated)[c(1,3)],
             ylim=st_bbox(output_rotated)[c(2,4)],
             crs=proj_rotated,
             expand = FALSE)+
    theme_dark()+
    theme(legend.position = c(1.64,0.2),
          legend.direction = "vertical",
          plot.margin = margin(t=5.5,b=5.5,l=0,r=140,unit = "pt"),
          legend.title = element_text(size=10))+
    guides(fill = guide_legend(title.position = "right",
                               reverse = TRUE))

ggsave("maps_for_pubs/base.png",base,height=6,width=4,dpi=600)


connect <- ggplot(oc_sfcon)+
    geom_sf(aes(fill=diff),colour="transparent")+
    scale_fill_distiller("Selection frequency\nhigher with\nconnectivity",palette=c("Oranges"),direction=1,limits=c(5,100))+
    coord_sf(xlim=st_bbox(output_rotated)[c(1,3)],
             ylim=st_bbox(output_rotated)[c(2,4)],
             crs=proj_rotated,
             expand = FALSE)+
    theme_dark()+
    theme(legend.position = c(1.64,0.8),
          legend.direction = "vertical",
          plot.margin = margin(t=5.5,b=5.5,l=0,r=140,unit = "pt"),
          legend.title = element_text(size=10),
          legend.background = element_rect(fill="transparent"),
          rect = element_rect(fill = "transparent"),
          panel.grid = element_line(colour="transparent"),
          panel.background = element_rect("transparent"),
          axis.ticks = element_line("transparent"),
          axis.text.x = element_text(colour="transparent"),
          axis.text.y = element_text(colour="transparent"))+
    guides(fill = guide_legend(title.position = "right",
                               reverse = TRUE))

ggsave("maps_for_pubs/connect.png",connect,bg="transparent",height=6,width=4,dpi=600)


categorical <- ggplot()+
    geom_sf(data=oc_greater90, aes(fill="A",colour="A"),size=0.3)+
    geom_sf(data=oc_bottom5, aes(fill="B",colour="B"),size=0.3)+
    scale_fill_manual("",values=c("#549b16","white"),labels=c("Always Irreplaceable","Rarely selected"))+
    scale_colour_manual("",values=c("#549b16","black"),labels=c("Always Irreplaceable","Rarely selected"))+
    coord_sf(xlim=st_bbox(output_rotated)[c(1,3)],
             ylim=st_bbox(output_rotated)[c(2,4)],
             crs=proj_rotated,
             expand = FALSE)+
    theme_dark()+
    theme(legend.position = c(1.6,0.5),
          legend.direction = "vertical",
          plot.margin = margin(t=5.5,b=5.5,l=0,r=140,unit = "pt"),
          legend.text = element_text(size=10),
          legend.background = element_rect(fill="transparent"),
          rect = element_rect(fill = "transparent",colour="transparent"),
          panel.grid = element_line(colour="transparent"),
          panel.background = element_rect("transparent"),
          plot.background = element_rect("transparent"),
          axis.ticks = element_line("transparent"),
          axis.text.x = element_text(colour="transparent"),
          axis.text.y = element_text(colour="transparent"))+
    guides(fill = guide_legend(title.position = "right"))

ggsave("maps_for_pubs/categorical.png",categorical,bg="transparent",height=6,width=4,dpi=600)


categorical <- image_read("maps_for_pubs/categorical.png")
con <- image_read("maps_for_pubs/connect.png")
base <- image_read("maps_for_pubs/base.png")
composite <- image_composite(image_composite(base,con),categorical)
composite
image_write(composite,"maps_for_pubs/diff.png")

#### bioregions ####

bio <- ggplot()+
    geom_sf(data=AUS,fill="grey",colour="transparent")+
    geom_sf(data=bioregions,aes(fill="A",colour="A"))+
    geom_sf(data=output_rotated,size=0.05,aes(fill="red",colour="red"))+
    facet_wrap(~ALT_LAB,nrow=2)+
    scale_fill_manual("",values=c("#1f78b4","transparent"),labels=c("Bioregion","Planning Units"))+
    scale_colour_manual("",values=c("transparent","black"),labels=c("Bioregion","Planning Units"))+
    coord_sf(xlim=st_bbox(output_rotated)[c(1,3)],
             ylim=st_bbox(output_rotated)[c(2,4)],
             crs=proj_rotated,
             expand = FALSE)+
    theme_dark()+
    theme(legend.position = "bottom",
          legend.direction = "horizontal")
ggsave("maps_for_pubs/bio_maps.png", bio,width=8.25,height=7.5,dpi=600)
