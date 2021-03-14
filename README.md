# Photo-Command

A simple terminal application of extensive photo editing made fast and easy

Photo-Command is a simple terminal application made in python for basic photo editing
It has a series of commands for the several procedures it can do

### Installation

``` % cd to the directory of installation ```

``` % git clone https://github.com/martin-otero/Photo-Command ```

``` % cd Photo-Command```

``` % python3 Photo-Command.py```

### Use

  * help → Returns help about the ussage of the program and all of it's functions
  * show → Displays the image being eddited in it's current state
  * save → Saves a copy of the image ( asks for name )
  * exit → Exits the program
  * exp → Modifies the image exposure
  * contrast → Modifies the image contrast
  * saturation → Modifies the color saturation
  * invert → Invert's the image's colors
  * blur → Blurs the image by the degree specified
  * channel → Modifies the intensitie of one of the RGB channels by the degree specified
  * grid → Creates a grid of points with specified color and distance

### Syntax

 #### → exp    
 *1st attribute* → declares wether the exposure is increased or decreased → options → ( + / - )       
 *2nd attribute* → declares by which degree the exposure is modified → range from 0 to infinite, but it's not recomended not to go above 6        

**Example** → ``` >> exp + 1.8 ```    


#### → contrast   
 *1st attribute* → declares wether the contrast is increased or decreased → options → ( + / - )   
 *2nd attribute* → declares by which degree the contrast is modified → range from 0 to infinite, but it's not recomended not to go above 2   
 
 **Example** → ``` >> contrast - 0.7 ```    
 
 #### → saturation    
 *1st attribute* → declares wether the contrast is increased or decreased → options → ( + / - )        
 *2nd attribute* → declares by which degree the contrast is modified → range from 0 to 255       
 
 *Example* → ``` >> saturation + 34 ```    
 
 #### → blur     
 *1st attribute* → declares how many times a 4-pixel average blur procedure will be executed ( the bigger this number, the most blured the image will apear )    
 **Note:** This process will take some time, especially when dealing with larger number of blur cicles. The cicles can be ilimited, but above 100 will take extremely long times even in high-end computers.    
 The number of blur cicles completed will be printed to keep track of the process
 
 **Example** → ``` >> blur 5 ``` 
 
 #### → channel
 *1st attribute* → declares which of the channels ( RGB ) is going to be modified 
 *2nd attribute* → declares the new value of that channel ( 0 - 1 )
 
 **Example** → ``` >>  channel R 0 ```                  
                ```>>  channel G 0.9``` 
                
 #### → grid
 *1st attribute* → declares de spacing between the points ( in pixels )
 *2nd attribute* → declares the color of the points ( 0 - 255 )
 **Note:** this one is easier to try out for yourself 
 
 **Example** → ``` >> grid 20 249 ``` 
 
 
 


      
  
