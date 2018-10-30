import random
import math

class cluster():
    def __init__(self):
        self.clusterObservations = []

    def getObservation(self):
        return self.clusterObservations

    def addObservation(self, observation):
        self.clusterObservations.append(observation)

    def removeObservation(self, observationLocation):
        self.clusterObservations.remove(observationLocation)

    def calculateCentroid(self, k):
        centroid = []
        centroidCounter = 0
        counter = 0
        max = 0
        while counter < len(self.clusterObservations):
            if((counter +1 == len(self.clusterObservations)) and (centroidCounter < k)):
                max = float(max + self.clusterObservations[counter][centroidCounter])
                counter+=1
                centroid.append(round(float(max / counter), 4))
                counter = 0
                centroidCounter+=1
                max = 0
            elif((counter+1 == len(self.clusterObservations) and (centroidCounter == k))):
                max = float(max + self.clusterObservations[counter][centroidCounter])
                counter+=1
                centroid.append(round(float(max / counter), 4))
                break
            else:
                max = float(max + self.clusterObservations[counter][centroidCounter])
                counter+=1

     

        return centroid


    def printCluster(self):
        return (self.clusterObservations)

    def getDimensions(self):
        return (len(self.clusterObservations))

class ClusterManager():
    def __init__(self, observations, k):
        self.observations = observations
        self.k = k
        self.clusters = []
        self.centroids = []

    def randomKMeansInitialization(self):
        for counter in range(self.k):
            self.clusters.append(cluster())

        for counter in range(len(self.observations)):
            self.clusters[random.randrange(self.k)].addObservation(self.observations[counter])

    def getClusters(self):
        return self.clusters

    def assignmentKMean(self):
        self.done = True
        for counter in range(len(self.clusters)):
         

            currentObservations = self.clusters[counter].getObservation()
            dynamicCounter = 0
            dynamicLength = len(currentObservations)
            while dynamicCounter < dynamicLength :
                for x in range(len(self.clusters)):
                    # print(dynamicCounter, dynamicLength)
                    euclideanDistance = self.calculateEuclideanObservationToCluster(currentObservations[dynamicCounter],self.clusters[x].calculateCentroid(self.k))
                    if(x == 0):
                        closest = euclideanDistance
                        closestclusterIndex = x
                        observationIndex = dynamicCounter
                    else:
                        if (closest > euclideanDistance):
                            closest = euclideanDistance
                            closestclusterIndex = x
                            observationIndex = dynamicCounter
                if(closestclusterIndex != counter):
                    self.clusters[closestclusterIndex].addObservation(currentObservations[observationIndex])
                    self.clusters[counter].removeObservation(currentObservations[observationIndex])
                    self.done = False
                    currentObservations = self.clusters[counter].getObservation()
                    dynamicLength = len(currentObservations)
                    dynamicCounter-=1

                dynamicCounter+=1

        return self.done


    def findNearestCluster(self, observation, clusterIndex):
        closestClusterIndex = 0
        currentClosestCluster = 0
        clusteringMap = []
      
        for counter in range(len(observation)):
            currentClosestCluster = 0
            for j in range(len(self.clusters)):
                if(currentClosestCluster == 0):
                    currentClosestCluster = (self.calculateEuclideanObservationToCluster(observation[counter], self.clusters[j].calculateCentroid(self.k)))
                    observationIndex = counter
                else:
                    temp = (self.calculateEuclideanObservationToCluster(observation[counter], self.clusters[j].calculateCentroid(self.k)))
                    if(currentClosestCluster > temp):
                        closestClusterIndex = j
                        observationIndex = counter

            if(closestClusterIndex != clusterIndex):
                self.clusters[closestClusterIndex].addObservation(observation[observationIndex])
                self.done = False
                clusteringMap.append(observationIndex)


        clusterRemover = len(clusteringMap)-1
        while clusterRemover > 0:
            self.clusters[clusterIndex].removeObservation(observation[clusteringMap[clusterRemover]])
            clusterRemover-=1

        for counter in range(self.k):
            print("--------------")
            print(self.clusters[counter].getObservation())



    def printClusters(self):
        files = open("testfile.txt", "w")
        for counter in range(len(self.clusters)):
            files.write("Cluster Number = "+ str(counter) + "\n")
            files.write(str(self.clusters[counter].getObservation()))
            files.write("\n")

    def calculateEuclideanObservationToCluster(self, observation, clusterCentroid):
        max = 0
        for counter in range(len(observation)):
            max+= math.pow((abs(clusterCentroid[counter] - observation[counter])), 2)
        euclidean = (round((float(math.sqrt(max))), 4))
        return euclidean

    def randomKMeansUpdate(self):
        self.centroids = []
        for counter in range(self.k):
            self.centroids.append(self.clusters[counter].calculateCentroid(self.k))



    def checkMissingObservations(self):
        max = 0
        for counter in range(self.k):
            max = max + self.clusters[counter].getDimensions()
        print(max)
