# generate landscape-based data for the demographic tutorial data
require(tidyverse)
require(sf)
# based on reefs
reefs <- st_read("tutorial/CSM_demographic/reefs.shp") %>%
    mutate(area = st_area(.))

distanceMatrix <- round(st_distance(reefs))


isolationMatrix <- 1/distanceMatrix^2 %>% matrix(nrow(reefs),nrow(reefs))

# remove links >200km
isolationMatrix[isolationMatrix<1/200000^2]=0

# create probability matrix
probabilityMatrix <- isolationMatrix

# add local recruitment
probabilityMatrix[is.infinite(probabilityMatrix)] <- max(probabilityMatrix[is.finite(probabilityMatrix)],na.rm = TRUE)/10^5
diag(probabilityMatrix) <- diag(probabilityMatrix)*sqrt(reefs$area)/mean(sqrt(reefs$area))

probabilityMatrix <- probabilityMatrix/rowSums(probabilityMatrix)
# write.csv(probabilityMatrix,"reefProb.csv")

# create flow matrix
fecundity <- as.numeric(reefs$area)
survival <- as.numeric(reefs$area/max(reefs$area))*0.0000001
flowMatrix <- t(t(probabilityMatrix)*survival)*fecundity
test <- runif(nrow(probabilityMatrix),0,1)<0.1
Re(eigen(flowMatrix[test,test])$values[1])
image(log(flowMatrix))

write.csv(flowMatrix,"tutorial/CSM_demographic/reefFlow.csv")

# based on hex
reefs <- st_read("tutorial/CF_demographic/hex_planning_units.shp") %>%
    mutate(area = st_area(.))

distanceMatrix <- round(st_distance(reefs))


isolationMatrix <- 1/distanceMatrix^2 %>% matrix(nrow(reefs),nrow(reefs))

# remove links >200km
isolationMatrix[isolationMatrix<1/200000^2]=0

# create probability matrix
probabilityMatrix <- isolationMatrix

# add local recruitment
probabilityMatrix[is.infinite(probabilityMatrix)] <- max(probabilityMatrix[is.finite(probabilityMatrix)],na.rm = TRUE)/10^5
diag(probabilityMatrix) <- diag(probabilityMatrix)*sqrt(reefs$area)/mean(sqrt(reefs$area))

probabilityMatrix <- probabilityMatrix/rowSums(probabilityMatrix)
# write.csv(probabilityMatrix,"reefProb.csv")

# create flow matrix
fecundity <- as.numeric(reefs$area)
survival <- as.numeric(reefs$area/max(reefs$area))*0.0000001
flowMatrix <- t(t(probabilityMatrix)*survival)*fecundity
test <- runif(nrow(probabilityMatrix),0,1)<0.1
Re(eigen(flowMatrix[test,test])$values[1])
image(log(flowMatrix))

write.csv(flowMatrix,"tutorial/CF_demographic/hexFlow.csv")

### make boundary.dat
reefs <- st_read("tutorial/CF_demographic/hex_planning_units.shp")

bound <- st_overlaps(reefs %>% st_buffer(1), sparse = FALSE) %>% 
    data.frame(check.names = FALSE) %>% 
    mutate(id1=row.names(.)) %>% 
    gather(key = 'id2', value='boundary',-id1) %>% 
    mutate(boundary=as.numeric(boundary)) %>% 
    filter(boundary>0)

write.csv(bound,"tutorial/CF_demographic/bound.dat")
