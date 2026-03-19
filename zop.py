from zopflipng import png_optimize

data = open("inputs/input2.png", "rb").read()
result,code = png_optimize(data)

if code == 0:
    open("outputs/zop_output2.png", "wb").write(result)