library(sf)
library(raster)
library(gridExtra)
library(tidyverse)

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
           best_solution = as.logical(best_solution),
           select_prob=select_freq/20) %>%
    st_as_sf() %>%
    left_join(puvspr_wide,by=c("pu_id"="pu"))%>% 
    st_transform(proj)

output_rotated <- st_transform(output,proj_rotated)


output_connect <- read.csv("maps_for_pubs/output/pu_connect.csv") %>%
    mutate(geometry=st_as_sfc(geometry,"+proj=longlat +datum=WGS84"),
           best_solution = as.logical(best_solution),
           select_prob=select_freq/20) %>%
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

bioregions$BIOREGI
plot_lyrs <- c("Planning Units","BIORE_27","BIORE_3","BIORE_26")
plot_brg <- bioregions %>% 
    filter(BIOREGI %in% plot_lyrs)

p1 <- ggplot(output_connect)+
    geom_sf(data=AUS,fill="grey",colour="transparent")+
    geom_sf(aes(fill=between_cent_land_pu_mean),colour="black",size=0.25)+
    scale_fill_distiller("Betweeness\nCentrality",palette="OrRd",direction = 1)+
    coord_sf(xlim=st_bbox(output_rotated)[c(1,3)],
             ylim=st_bbox(output_rotated)[c(2,4)],
             crs=proj_rotated,
             expand = FALSE)+
    theme(legend.position = "bottom",
          legend.direction = "vertical",
          legend.background = element_rect(fill="transparent"),
          plot.title = element_text(size=10))+
    ggtitle("A) Connect. Feature")

p2 <- ggplot(output)+
    geom_sf(data=AUS,fill="grey",colour="transparent")+
    geom_sf(aes(fill=select_freq/20*100),colour="black",size=0.25)+
    scale_fill_distiller("Selection\nFrequency (%)",palette="BuGn",direction = 1,limits=c(0,100))+
    coord_sf(xlim=st_bbox(output_rotated)[c(1,3)],
             ylim=st_bbox(output_rotated)[c(2,4)],
             crs=proj_rotated,
             expand = FALSE)+
    theme(legend.position = "bottom",
          legend.direction = "vertical",
          legend.background = element_rect(fill="transparent"),
          plot.title = element_text(size=10))+
    ggtitle("B) Without Connectivity")
          

p3 <- ggplot(output_connect)+
    geom_sf(data=AUS,fill="grey",colour="transparent")+
    geom_sf(aes(fill=select_freq/20*100),colour="black",size=0.25)+
    scale_fill_distiller("Selection\nFrequency (%)",palette="BuGn",direction = 1,limits=c(0,100))+
    coord_sf(xlim=st_bbox(output_rotated)[c(1,3)],
             ylim=st_bbox(output_rotated)[c(2,4)],
             crs=proj_rotated,
             expand = FALSE)+
    theme(legend.position = "bottom",
          legend.direction = "vertical",
          legend.background = element_rect(fill="transparent"),
          plot.title = element_text(size=10))+
    ggtitle("C) With Connectivity")

output_connect$diff <- output_connect$select_freq-output$select_freq


p4 <-
ggplot(output_connect)+
    geom_sf(data=AUS,fill="grey",colour="transparent")+
    geom_sf(aes(fill=diff/20*100),colour="black",size=0.25)+
    scale_fill_distiller("Connectivity\nDifference",palette="BrBG",direction = 1,limits=c(-100,100))+
    coord_sf(xlim=st_bbox(output_rotated)[c(1,3)],
             ylim=st_bbox(output_rotated)[c(2,4)],
             crs=proj_rotated,
             expand = FALSE)+
    theme(legend.position = "bottom",
          legend.direction = "vertical",
          legend.background = element_rect(fill="transparent"),
          plot.title = element_text(size=10))+
    ggtitle("D) Difference")

ggsave("maps_for_pubs/maps.png", grid.arrange(p1, p2, p3, p4, ncol=4),width=7.5,height=7.5,dpi=600)




bio <- ggplot()+
    geom_sf(data=AUS,fill="grey",colour="transparent")+
    geom_sf(data=bioregions,aes(fill="A",colour="A"))+
    geom_sf(data=output_rotated,size=0.25,aes(fill="red",colour="red"))+
    facet_wrap(~ALT_LAB,nrow=2)+
    scale_fill_manual("",values=c("#1f78b4","transparent"),labels=c("Bioregion","Planning Units"))+
    scale_colour_manual("",values=c("transparent","black"),labels=c("Bioregion","Planning Units"))+
    coord_sf(xlim=st_bbox(output_rotated)[c(1,3)],
             ylim=st_bbox(output_rotated)[c(2,4)],
             crs=proj_rotated,
             expand = FALSE)+
    theme(legend.position = "bottom",
          legend.direction = "horizontal")
ggsave("maps_for_pubs/bio_maps.png", bio,width=8.25,height=7.5,dpi=600)
