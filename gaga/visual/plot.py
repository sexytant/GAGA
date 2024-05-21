from gaga.general.express import Express
from gaga.visual.component import Shape,Image
from gaga.general.component import Population
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb
import matplotlib.patches as patches
from multiprocessing import Process


class Plot(Express):
    def expressCodon(self,shape:Shape):
        if shape.type=="Ellipse":
            x=shape.basis["x"].letter
            y=shape.basis["y"].letter
            width=shape.basis["width"].letter
            height=shape.basis["height"].letter
            red=shape.basis["red"].letter
            green=shape.basis["green"].letter
            blue=shape.basis["blue"].letter
            return patches.Ellipse((x,y),width,height,color=to_rgb((red,green,blue)))
    def plotShape(self,shape:Shape):
        return self.expressCodon(shape)

    def expressIndividual(self,image: Image,size: int,index: int):
        ax=plt.subplot(1,size,index+1)
        for shape in image.gene:
            ax.add_artist(self.plotShape(shape))
        ax.axis("off")
        ax.set_title(str(image.displayName))

    def plotImage(self,generation: int,image:Image,size: int,index: int):
        self.expressIndividual(image,size,index)
        #plt.savefig("../results/{generation}_{id}".format(generation=generation,id=image.id))

    def expressPopulation(self, population: Population):
        print("generation:%s" % population.generation)
        plt.figure(figsize=(4*population.size,3))
        for i in range(population.size):
            self.plotImage(population.generation,
                            population.individuals[i],
                            population.size,
                            i
                            )
        plt.show()
