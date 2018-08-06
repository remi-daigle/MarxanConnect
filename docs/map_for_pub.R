# CF_landscape maps for publication
library(sf)
library(raster)
library(gridExtra)
library(tidyverse)


# set default projection for leaflet
proj <- "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +wktext  +no_defs"
proj_rotated <- "+proj=omerc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +wktext  +no_defs +alpha=-73.00000"

spec <- read.csv("tutorial/CF_landscape/input/spec.dat")
puvspr <- read.csv("tutorial/CF_landscape/input/puvspr2.dat")
pu <- read.csv("tutorial/CF_landscape/input/pu.dat")

puvspr_wide <- puvspr %>%
    left_join(select(spec,"id","name"),
              by=c("species"="id")) %>%
    select(-species) %>%
    spread(key="name",value="amount")

# planning units with output
output <- read.csv("tutorial/CF_landscape/output/pu_no_connect.csv") %>%
    mutate(geometry=st_as_sfc(geometry,"+proj=longlat +datum=WGS84"),
           best_solution = as.logical(best_solution)) %>%
    st_as_sf() %>%
    left_join(puvspr_wide,by=c("pu_id"="pu"))%>% 
    st_transform(proj)

output_rotated <- st_transform(output,proj_rotated)


output_connect <- read.csv("tutorial/CF_landscape/output/pu_connect.csv") %>%
    mutate(geometry=st_as_sfc(geometry,"+proj=longlat +datum=WGS84"),
           best_solution = as.logical(best_solution)) %>%
    st_as_sf() %>%
    left_join(puvspr_wide,by=c("pu_id"="pu"))%>% 
    st_transform(proj) 

bioregions <- st_read("tutorial/CF_landscape/bioregion_short.shp",stringsAsFactors = FALSE) %>% 
    st_transform(proj) %>% 
    mutate(BIOREGI=paste0("BIORE_",BIOREGI)) %>% 
    filter(BIOREGI %in% spec$name) %>% 
    group_by(BIOREGI) %>% 
    summarize() %>% 
    mutate(BIOREGI=as.character(BIOREGI))

bioregions[nrow(bioregions)+1,] <- st_as_sf(data.frame(BIOREGI="Planning Units",geometry=st_combine(output)))
bioregions$BIOREGI[nrow(bioregions)]="Planning Units"

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

p1 <- ggplot(plot_brg)+
    geom_sf(data=AUS,fill="grey",colour="transparent")+
    geom_sf(aes(fill=BIOREGI,colour=BIOREGI),size=0.25)+
    scale_fill_manual("Type\n",values=c("#a6cee3","#1f78b4","#b2df8a","transparent"))+
    scale_colour_manual("Type\n",values=c("transparent","transparent","transparent","black"))+
    coord_sf(xlim=st_bbox(output_rotated)[c(1,3)],
             ylim=st_bbox(output_rotated)[c(2,4)],
             crs=proj_rotated,
             expand = FALSE)+
    theme(legend.position = "bottom",
          legend.direction = "vertical",
          legend.margin = margin(14 , 6, 14 , 6),
          legend.background = element_rect(fill="transparent"),
          plot.title = element_text(size=10))+
    ggtitle("A) Representation Data")

p2 <- ggplot(output)+
    geom_sf(data=AUS,fill="grey",colour="transparent")+
    geom_sf(aes(fill=google_land_pu_R),colour="black",size=0.25)+
    scale_fill_distiller("Selection\nFrequency",palette="OrRd",direction = 1,limits=c(0,0.007))+
    coord_sf(xlim=st_bbox(output_rotated)[c(1,3)],
             ylim=st_bbox(output_rotated)[c(2,4)],
             crs=proj_rotated,
             expand = FALSE)+
    theme(legend.position = "bottom",
          legend.direction = "vertical",
          legend.background = element_rect(fill="transparent"),
          plot.title = element_text(size=10))+
    ggtitle("B) Google PageRank")

p3 <- ggplot(output)+
    geom_sf(data=AUS,fill="grey",colour="transparent")+
    geom_sf(aes(fill=select_freq),colour="black",size=0.25)+
    scale_fill_distiller("Selection\nFrequency",palette="BuGn",direction = 1,limits=c(0,20))+
    coord_sf(xlim=st_bbox(output_rotated)[c(1,3)],
             ylim=st_bbox(output_rotated)[c(2,4)],
             crs=proj_rotated,
             expand = FALSE)+
    theme(legend.position = "bottom",
          legend.direction = "vertical",
          legend.background = element_rect(fill="transparent"),
          plot.title = element_text(size=10))+
    ggtitle("C) Without Connectivity")
          

p4 <- ggplot(output_connect)+
    geom_sf(data=AUS,fill="grey",colour="transparent")+
    geom_sf(aes(fill=select_freq),colour="black",size=0.25)+
    scale_fill_distiller("Selection\nFrequency",palette="BuGn",direction = 1,limits=c(0,20))+
    coord_sf(xlim=st_bbox(output_rotated)[c(1,3)],
             ylim=st_bbox(output_rotated)[c(2,4)],
             crs=proj_rotated,
             expand = FALSE)+
    theme(legend.position = "bottom",
          legend.direction = "vertical",
          legend.background = element_rect(fill="transparent"),
          plot.title = element_text(size=10))+
    ggtitle("D) With Connectivity")


ggsave("maps.png", grid.arrange(p1, p2, p3, p4, ncol=4),width=7.5,height=7.5,dpi=600)


