from tkinter import Tk, Canvas, PhotoImage

class AnimationController:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.geometry(f"{width}x{height}")
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack()

        self.animations = []

    def add_animation(self, animation):
        self.animations.append(animation)

    def start_animations(self):
        for animation in self.animations:
            animation.start(self.canvas)

        self.root.mainloop()

class Animation:
    def __init__(self, image_files, x, y):
        self.images = []
        for image_file in image_files:
            image = PhotoImage(file=image_file)
            self.images.append(image)

        self.x = x
        self.y = y
        self.current_image = None

    def start(self, canvas):
        self.canvas = canvas
        self.current_image = self.canvas.create_image(self.x, self.y, image=self.images[0])

        self.animate(0)

    def animate(self, index):
        if index < len(self.images):
            self.canvas.itemconfig(self.current_image, image=self.images[index])
            self.canvas.after(1000, self.animate, index + 1)

# Example usage
if __name__ == '__main__':
    animation_controller = AnimationController(800, 600)

    # Example animation 1: Blinking Eyes
    blinking_eyes_animation = Animation(["eye_open.png", "eye_closed.png"], 400, 300)
    animation_controller.add_animation(blinking_eyes_animation)

    # Example animation 2: Moving Object
    moving_object_animation = Animation(["object_frame1.png", "object_frame2.png", "object_frame3.png"], 200, 200)
    animation_controller.add_animation(moving_object_animation)

    animation_controller.start_animations()
