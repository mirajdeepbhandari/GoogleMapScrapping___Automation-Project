from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from scraping import main


def handle_inputs():
    place_name = place_input.get()
    keyword = keyword_input.get()

    if not place_name:
        messagebox.showerror('Input Error', 'Place Name is required.')
        return
    if not keyword:
        messagebox.showerror('Input Error', 'Keyword is required.')
        return
    
    # Write place_name and keyword to a file
    with open('place_and_keyword.txt', 'w') as file:
        file.write(f"{place_name}\n{keyword}")

    messagebox.showinfo('Success', f'Scraping data for {place_name} with keyword {keyword}')
    main()
    messagebox.showinfo('Success', f'Scraping is Finished. Check the output folder.')



root = Tk()

root.title('Map Scraping Tool')
root.geometry('800x600')
root.configure(background='#ecf0f1')

# Load and resize the image
img = Image.open('wallpapers/img1.jpg')
resized_img = img.resize((120, 120))
img = ImageTk.PhotoImage(resized_img)

# Create a Label widget and set the image
label = Label(root, image=img)
label.pack(pady=(20,10))

# Keep a reference to the image object to avoid garbage collection
label.image = img

text_label = Label(root, text='....MAP SCRAPPING....', fg='white', bg='#0096DC')
text_label.pack(fill='x', pady=(20,15))
text_label.config(font=('verdana',15))

place_label = Label(root, text='Enter Place Name: ', fg='white', bg='#e74c3c')
place_label.pack(pady=(20,10))
place_label.config(font=('verdana',14))

place_input = Entry(root, width=50)
place_input.pack(ipady=10, pady=(5,15))

keyword_label = Label(root, text='Enter Keyword: ', fg='white', bg='#e74c3c')
keyword_label.pack(pady=(20,10))
keyword_label.config(font=('verdana',14))

keyword_input = Entry(root, width=70)
keyword_input.pack(ipady=10, pady=(5,15))

submit_btn = Button(root, text='Scrape', bg='#2c3e50', fg='white', width=20, height=2, command=handle_inputs)
submit_btn.pack(pady=(30,70))
submit_btn.config(font=('verdana',10))

root.mainloop()
