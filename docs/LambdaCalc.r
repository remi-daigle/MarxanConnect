# Calculate Metapopulation Lambda values
# originally from EcoTraps code, 9Mar2014 -etreml
# adapted from Figueira & Crowder 2006
#  updated for colSums and rviewed by JohnFord.
#
#input
# 1. Conmat = row-normalised connectivity matrix (row as sources)
# 2. size = size of habitat patches, same size
# 3. fec = fecundity per individual in patch (including impact of quality) as vector, same size as rows in Conmat
# 4. surv = surivorship [0-1] for each patch (including impact of quality), same size as above
#
#output
# 1. id = node ids
# 2. selfR = proportion self-recruitment from Migration matrix
# 3. SetH = settler Diversity
# 4. LambdaC = contributuion Lambda (F & C 2006)
# 5. rNt = relative patch population sizes (size*qual/sum(size*qual))
# 6. LambdaCp = proportional contribution to Lambda-M
# 7. LambdaM = Metapopulation Lambda
# 8. Mmat = migration matrix (rows as sources)

LambdaCalc <- function(ConMat, size, fec, surv) {
  n<-length(size)
  #Self Recruitment & Diversity Calc
  RO<-as.matrix(size*fec)                 # Reproductive output or source strength
  RO.m<-RO[,rep(1,n)]
  FMat<-ConMat*RO.m                       # Flux matrix (Source as rows)
  csFMat<-t(as.matrix(colSums(FMat)))     # t() to make row vector
  MMat<-FMat/csFMat[rep(1,n),]            # Migration matrix (Source as rows)
  SelfR<-diag(MMat)                       # Self-recruitment
  logMMat<-log(MMat,10)
  H<-colSums(MMat*logMMat,1)*-1           # Diversity of settlers
  # Lambda Calc
  tPMat<-t(ConMat)                        # Now Sources are COLUMNS (as in F&C 2006)
  si<-as.matrix(surv)                     # Settler survival per destination
  si.m<-si[,rep(1,n)]
  siPji.m<-tPMat*si.m                     # Downstream contribution of post-settler survivors
  #   siPji.rs<-rowSums(siPji.m)              # Sum sj*Pji across sources for each destination (row)
  siPji.cs<-colSums(siPji.m)              # Sum sj*Pji across destinations for each source (col)
  LambdaC<-as.matrix(surv + siPji.cs*fec) # (F&C 2006, Eq. 19)
  # rNt<-as.matrix(size*qual/sum(size*qual)) #qual not passed to function, used trap qual
  rNt<-as.matrix(size*fec/sum(size*fec))
  LambdaM<-colSums(LambdaC*rNt)           # Lambda-M  (F&C 2006, Eq. 13)
  LambdaCp<-(LambdaC*rNt)/LambdaM         # Lambda-C (per patch) proportional contribution
  
  outList<- list("id" = rownames(ConMat), "selfR" = SelfR, "SetH" = H, "LambdaC" = LambdaC, "rNt" = rNt,
    "LambdaCp" = LambdaCp, "LambdaM" = LambdaM, "Mmat" = MMat)
  
  return(outList)
}
  
