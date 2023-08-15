        line_spacing = 10

        # Calculate the position of the text in the center of the image
        x = (img.width - draw.textbbox((0, 0), wrapped_text[0], font=font)[2]) // 2
        y = (img.height - ((font.getsize(wrapped_text[0])[1] + line_spacing) * len(wrapped_text))) // 2

        # Draw each line of wrapped text on the image
        for line in wrapped_text:
            text_width, text_height = draw.textsize(line, font=font)
            draw.text(((img.width - text_width) // 2, y), line, fill='white', font=font, outline='black')
            y += text_height + line_spacing
