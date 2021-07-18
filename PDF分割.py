#!/usr/bin/env python
# coding: utf-8

# #PDFを分割

# In[2]:


import glob,os,sys


# In[3]:


# モジュールのインポート
import os, tkinter, tkinter.filedialog, tkinter.messagebox


# In[4]:


# ファイル選択ダイアログの表示
root = tkinter.Tk()
root.withdraw()
fTyp = [("PDF","*.pdf")]
#iDir = os.path.abspath(os.path.dirname(os.getcwd()))
iDir = os.path.abspath(os.path.dirname(sys.executable))
#os.chdir(os.path.dirname(os.path.abspath(__file__)))
#tkinter.messagebox.showinfo('○×プログラム','処理ファイルを選択してください！')
file = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)


# In[5]:


print(file)


# In[6]:


if file == "":
    sys.exit(1)


# In[7]:


import PyPDF2


# In[8]:


from PyPDF2 import PdfFileWriter, PdfFileReader


# In[9]:


reader = PyPDF2.PdfFileReader(file)


# In[10]:


reader


# In[11]:


page_nums =reader.getNumPages()


# In[12]:


print(page_nums)


# In[13]:


(name, extention) = os.path.splitext(file)


# In[14]:


for num in range(page_nums):
    file_object = reader.getPage(num)
    pdf_file_name = name + '-' + str(num+1) + '.pdf'
    pdf_file_writer = PdfFileWriter()
    with open(pdf_file_name,'wb') as f:
        pdf_file_writer.addPage(file_object)
        pdf_file_writer.write(f)


# In[15]:


tkinter.messagebox.showinfo('PDF分割','PDFファイルの分割が終わりました！')


# In[ ]:




