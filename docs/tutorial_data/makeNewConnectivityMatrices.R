# generate landscape-based data for the demographic tutorial data
require(tidyverse)
require(sf)
# based on reefs
reefs <- st_read("tutorial_data/CSM_demographic/reefs.shp") %>%
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

write.csv(flowMatrix,"tutorial_data/CSM_demographic/reefFlow.csv")

# based on hex
reefs <- st_read("tutorial_data/CF_demographic/hex_planning_units.shp") %>%
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

write.csv(flowMatrix,"tutorial_data/CF_demographic/hexFlow.csv")