import colorgram as cg


class CreateColors:

    def __init__(self, image, number_of_colors):
        self.color_list = cg.extract(image, number_of_colors)
        self.colors_palette = []

    def create_palette(self):
        for color in range(len(self.color_list)):
            rgb_colors = self.color_list[color]
            color = (rgb_colors.rgb.r, rgb_colors.rgb.g, rgb_colors.rgb.b)
            self.colors_palette.append(color)
        return self.colors_palette
