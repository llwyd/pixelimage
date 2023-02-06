from PIL import Image, ImageEnhance
import numpy as np

square_size = 75
bands = 3

with Image.open("blackbird.jpg") as im:
    px = im.load()

    w = im.size[0]
    h = im.size[1]

    w_smol = int(im.size[0] / square_size )
    h_smol = int(im.size[1] / square_size )
    
    print(f"Original Size:  {w}*{h}" )
    print(f"     New Size:  {w_smol}*{h_smol}" )

    x = np.zeros([w_smol,h_smol,bands],dtype=np.uint32)

    for i in range( w ):
        for j in range( h ):
            i_smol = int(i/square_size)
            j_smol = int(j/square_size)

            x[i_smol][j_smol][0] += px[i,j][0]
            x[i_smol][j_smol][1] += px[i,j][1]
            x[i_smol][j_smol][2] += px[i,j][2]

    x = np.floor_divide(x,square_size**2)

    new_out = Image.new( 'RGB', (w,h) )
    new_px = new_out.load()
    
    for i in range( w ):
        for j in range( h ):
            i_smol = int(i/square_size)
            j_smol = int(j/square_size)

            new_px[i,j] = ( x[i_smol][j_smol][0],x[i_smol][j_smol][1],x[i_smol][j_smol][2])


    convertor = ImageEnhance.Contrast(new_out)
    new_out = convertor.enhance(1)
    convertor = ImageEnhance.Sharpness(new_out)
    new_out = convertor.enhance(1)
    convertor = ImageEnhance.Color(new_out)
    new_out = convertor.enhance(1)

    new_out.show()
