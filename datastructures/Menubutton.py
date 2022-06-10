
class MenuButton:
	def __init__(self, pos_x, pos_y, text_input, font, base_color ="Black", hovering_color="White"):
		self.x_pos = pos_x
		self.y_pos = pos_y
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		"""Putting the button on the screen"""
		screen.blit(self.text, self.text_rect)

	def checkMouseClick(self, mousePositionX, mousePositionY):
		"""Check the mouse position , if it is within the area of the button or not"""
		if mousePositionX in range(self.text_rect.left, self.text_rect.right) and mousePositionY in range(self.text_rect.top, self.text_rect.bottom):
			return True
		return False

	def changeColor(self, mousePositionX, mousePositionY):
		"""Changing the color of the button, if the mouse is hovering over the button"""
		if mousePositionX in range(self.text_rect.left, self.text_rect.right) and mousePositionY in range(self.text_rect.top, self.text_rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

