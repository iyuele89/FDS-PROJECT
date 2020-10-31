# FDS-PROJECT

1. **Image Filtering (10 points)**\
1.d What happens when you apply the following Filter combinations? 
    
    1. *First Gx, then GxT*\
    **First we smooth the image in the horizontal direction by applying the single-dimensional Gaussian matrices Gx, then then we repeat the process in the vertical direction 
    Gy = Gx^T. It has the same effect of applying a two-dimensional gaussian matrix because the gaussian filter is a separable one. In computational terms, applying  the
    independent one-dimensional filter is more efficient, since the calculation can be performed in O(n) rather than O(n^2).
    Each pixels of the blurred image are set to a weighted average of that pixel’s neighborhood. The original pixel's value receives the heaviest weight
    (having the highe Gaussian value) and neighboring pixels receive smaller weights as their distance to the original pixel increases.**
    
    2. *First Gx, then DxT*\
    **First we filter the image in the horizontal direction by applying Gx and this will give us pixels with higher intensity at the img_imp [13, 13] where we have the impulse
    and gets less brighter as the neighboring pixels receive smaller weights as their distance to the original pixel increases. When then we apply the derivative filter in 
    the vertical direction what happens is that it detects edges in the horizontal direction by increasing and decreasing the intensity of pixels below and above the 
    edge, respectively.**

    
    3. *First DxT , then Gx*\
    **This filter combination has the same effect of question number two because of the linear operation of convolution and derivative, therefor applying first the 
    derivative filter and then the smoothing operation or vice versa is not going to change the final output image.**
    
    4. *First Dx, then DxT*\
    **By applying a first order differentiation in horizontal and vertical direction we detect vertical edges and horizontal edges respectively, so Dx sets pixels with 
    higher intensity to the right of the edge and darker to the left and when we apply the Dy it detects horizontal edges by giving highest gaussian value to pixels bellow 
    the edge and smaller weight to those above.**
    
    5. *First Dx, then GxT*\
    **Here the one dimensional gaussian filter is smoothing in the horizontal direction (in general filter the high frequency pixels) followed by a first order differentiation 
    in y direction (Gx^T = Gy), which attributes highest gaussian values to pixels positioned right to the edges and low values to those in the left.**
    
    6. *First GxT , then Dx*\
    **This combination has the same effect as question number five, because of the linear property of derivative and convolution operation.**

2. **Image Representations, Histogram Distances (10 points)**

3. **Object Identification (10 points)**

4. **Performance Evaluation (bonus question for 10 points, not compulsory)**
