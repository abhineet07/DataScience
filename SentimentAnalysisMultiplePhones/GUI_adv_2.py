from tkinter import *
import tkinter.ttk as ttk
# from Amazon import *
from Amazon2 import *
from SmartPrixAnalytics2 import *
from Mobile91Analytics2 import *
from IndiaTodayAnalytics2 import *
from PhoneCurryAnalytics2 import *
from ExcelWriter import *
from Flipkart3 import *
from FeatureWiseAnalysis2 import *
import os
from Controller import *
import queue
from threading import Thread
import xlsxwriter


class InterFace:
    def __init__(self, root):
        self.root = root
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)

        self.que = queue.Queue
        # self.root.grid_columnconfigure(1, weight=1)

        # self.frame1 = Frame(root, background="Blue")
        # self.frame2 = Frame(root, background="Red")
        # self.frame3 = Frame(root, background="cyan")
        # self.frame4 = Frame(root, background="White")

        self.frame1 = Frame(root)
        self.frame2 = Frame(root)
        self.frame3 = Frame(root, background="White")
        self.frame4 = Frame(root)

        self.frame1.grid(row=0, column=0, sticky="nsew")
        self.frame2.grid(row=1, column=0, sticky="nsew")
        self.frame4.grid(row=2, column=0, sticky="nsew")
        self.frame3.grid(row=0, column=1, rowspan=3, sticky="nsew")


        ########################## FRAME - 1 ###############################################
        self.label_website = ttk.Label(self.frame1, text='Select Website')
        self.variable2 = StringVar(self.frame1)
        self.variable2.set("Amazon")
        options1 = ['ALL', 'Amazon', 'Flipkart', 'SmartPrix',
                                        'IndiaToday', '91mobiles', 'PhoneCurry']
        self.dropdown1 = ttk.OptionMenu(self.frame1, self.variable2, 'ALL', *options1)
        self.dropdown1.config(width=10)

        self.label_brand = ttk.Label(self.frame1, text='Select Brand')
        self.variable1 = StringVar(self.frame1)
        self.variable1.set("Samsung")
        options2 = ['Samsung', 'Vivo', 'Xiomi', 'Huawei', 'Realme']
        self.dropdown2 = ttk.OptionMenu(self.frame1, self.variable1, 'Samsung', *options2)
        self.dropdown2.config(width=10)

        self.label_pages = ttk.Label(self.frame1, text='Enter Pages')
        self.entry_pages = ttk.Entry(self.frame1)
        self.label_model = ttk.Label(self.frame1, text='Enter Model')
        self.entry_model = ttk.Entry(self.frame1)
        self.label_url = ttk.Label(self.frame1, text='Enter URL')
        self.entry_url = ttk.Entry(self.frame1)

        self.load_button = ttk.Button(self.frame1, text="Load", command=self.loadFile)
        self.open_excel_button = ttk.Button(self.frame1, text="Open Excel", command=self.openExcelFile)
        self.runByName_button = ttk.Button(self.frame1, text="Run By Name", command=self.getPath)
        self.runByURL_button = ttk.Button(self.frame1, text="Run By URL", command=self.analyseByURL)

        self.label_website.grid(row=0, column=0, padx=7, pady=7, sticky="w")
        self.label_brand.grid(row=1, column=0, padx=7, pady=7, sticky="w")
        self.dropdown1.grid(row=0, column=1, padx=7, pady=7, sticky="w")
        self.dropdown2.grid(row=1, column=1, padx=7, pady=7, sticky="w")
        self.label_pages.grid(row=2, column=0, padx=7, pady=7, sticky="w")
        self.entry_pages.grid(row=2, column=1, padx=7, pady=7)
        self.label_model.grid(row=3, column=0, padx=7, pady=7, sticky="w")
        self.entry_model.grid(row=3, column=1, padx=7, pady=7)
        self.runByName_button.grid(row=3, column=2, padx=7, pady=7)
        self.label_url.grid(row=4, column=0, padx=7, pady=7, sticky="w")
        self.entry_url.grid(row=4, column=1, padx=7, pady=7)
        self.runByURL_button.grid(row=4, column=2, padx=7, pady=7)
        self.load_button.grid(row=5, column=0, padx=7, pady=7, sticky="e")
        self.open_excel_button.grid(row=5, column=1, padx=7, pady=7, sticky="e")
        ############################### FRAME-1 ENDS ######################################

        ################################ FRAME-2 STARTS ###################################
        self.label_select_fetures = ttk.Label(self.frame2, text="Select Features :")
        self.camera_var = IntVar()
        self.check_camera = ttk.Checkbutton(self.frame2, text="Camera", variable=self.camera_var)
        self.display_var = IntVar()
        self.check_display = ttk.Checkbutton(self.frame2, text="Display", variable=self.display_var)
        self.finger_var = IntVar()
        self.check_finger = ttk.Checkbutton(self.frame2, text="Finger Print", variable=self.finger_var)
        self.battery_var = IntVar()
        self.check_battery = ttk.Checkbutton(self.frame2, text="Battery", variable=self.battery_var)
        self.button_analyse = ttk.Button(self.frame2, text="Analyse", command=self.AnalyseReport)

        self.label_showResults = ttk.Label(self.frame2, text="Select a feture to view results :")
        self.option = StringVar()
        self.radio_camera = ttk.Radiobutton(self.frame2, text="Camera", value="Camera", var=self.option)
        self.radio_display = ttk.Radiobutton(self.frame2, text="Display", value="Display", var=self.option)
        self.radio_finger = ttk.Radiobutton(self.frame2, text="Finger Print", value="Finger Print", var=self.option)
        self.radio_battery = ttk.Radiobutton(self.frame2, text="Battery", value="Battery", var=self.option)
        self.button_showResults = ttk.Button(self.frame2, text="Show Results", command=self.PrintResults)

        self.label_select_fetures.grid(row=0, column=0, padx=7, pady=7, sticky="w")
        self.check_camera.grid(row=1, column=0, padx=7, pady=7, sticky="w")
        self.check_display.grid(row=1, column=1, padx=7, pady=7, sticky="w")
        self.check_finger.grid(row=1, column=2, padx=7, pady=7, sticky="w")
        self.check_battery.grid(row=1, column=3, padx=7, pady=7, sticky="w")
        self.button_analyse.grid(row=2, column=0, padx=7, pady=7, sticky="w")

        self.label_showResults.grid(row=3, column=0, padx=7, pady=7, sticky="w")
        self.radio_camera.grid(row=4, column=0, padx=7, pady=7, sticky="w")
        self.radio_display.grid(row=4, column=1, padx=7, pady=7, sticky="w")
        self.radio_finger.grid(row=4, column=2, padx=7, pady=7, sticky="w")
        self.radio_battery.grid(row=4, column=3, padx=7, pady=7, sticky="w")
        self.button_showResults.grid(row=5, column=0, padx=7, pady=7, sticky="w")
        ########################### FRAME-2 Ends ###############################


        ########################### FRAMES-3 START #############################
        self.select_ftr_label = ttk.Label(self.frame3, text="Feature : ")
        self.select_polarity_label = ttk.Label(self.frame3, text="Polarity : ")

        self.variable3 = StringVar(self.frame1)
        self.variable3.set("Camera")
        options3 = ['Camera', 'Display', 'FingerPrint', 'Battery']
        self.select_ftr_dropdown = ttk.OptionMenu(self.frame3, self.variable3, 'Camera', *options3)

        self.variable4 = StringVar(self.frame1)
        self.variable4.set("ALL")
        options4 = ['ALL', 'Positive', 'Negative', 'Uncategorized']
        self.select_polarity_dropdown = ttk.OptionMenu(self.frame3, self.variable4, 'ALL', *options4)

        self.loadComment_Button = ttk.Button(self.frame3, text="Load Comments", command=self.getComments)

        self.comment_text = Text(self.frame3, wrap=WORD)
        self.scrollbar = Scrollbar(self.frame3, command=self.comment_text.yview)
        self.comment_text['yscrollcommand'] = self.scrollbar.set

        self.prev_button = ttk.Button(self.frame3, text="Previous", command=self.onPervClick)
        self.next_button = ttk.Button(self.frame3, text="Next", command=self.onNextClick)

        self.select_ftr_label.grid(row=0, column=0, padx=7, pady=7, sticky="e")
        self.select_ftr_dropdown.grid(row=0, column=1, padx=7, pady=7, sticky="w")
        self.select_polarity_label.grid(row=1, column=0, padx=7, pady=7, sticky="e")
        self.select_polarity_dropdown.grid(row=1, column=1, padx=7, pady=7, sticky="w")
        self.loadComment_Button.grid(row=2, column=0, columnspan=2, padx=7, pady=7)
        self.comment_text.grid(row=3, column=0, columnspan=2, padx=7, pady=7, sticky="e")
        self.scrollbar.grid(row=3, column=2, sticky="nsew")
        self.prev_button.grid(row=4, column=0, padx=7, pady=7, sticky="e")
        self.next_button.grid(row=4, column=1, padx=7, pady=7, sticky="w")
        ############################ FRAME-3 ENDS #############################


    ############################################################################
    ############################## FUNCTIONALITY ###############################
    ############################################################################
    def function(self):
        print("Hello World")

    def loadFile(self):
        self.model = str(self.entry_model.get())
        print(self.model)

        self.brand = self.variable1.get()
        print("Brand : ", self.brand)

        self.fileName = "Reviews_" + self.brand + "_" + self.model + ".xlsx"

    def getPath(self):
        print("####################################################")
        print("####################################################")
        print("\n")
        self.model = str(self.entry_model.get())
        print(self.model)

        self.brand = self.variable1.get()
        print("Brand : ", self.brand)

        self.website = self.variable2.get()
        print("Website : ", self.website)

        self.pages = int(self.entry_pages.get())
        print("Pages : ", self.pages)

        # print(self.query)

        if self.website == "ALL":
            print(">>>\n Analysing Amazon")
            self.AmazonCall()
            print(">>>\n Analysing Flipkart")
            self.FlipkartCall()
            print(">>>\n Analysing SmartPrix")
            self.SmartprixCall()
            print(">>>\n Analysing Mobiles 91")
            self.Mobiles91Call()
            print(">>>\n Analysing India Today")
            self.IndiaTodayCall()
            print(">>>\n Analysing Phone Curry")
            self.PhoneCurryCall()

            print(">>>\n Done.")

        elif self.website == "Amazon":
            t = Thread
            self.AmazonCall()

        elif self.website == "Flipkart":
            # t = Thread(target=self.FlipkartCall())
            # t.start()
            # t.join()
            print("1. CALLING FLIPKART")
            self.FlipkartCall()

        elif self.website == "SmartPrix":
            self.SmartprixCall()

        elif self.website == "91mobiles":
            self.Mobiles91Call()

        elif self.website == "IndiaToday":
            self.IndiaTodayCall()

        elif self.website == "PhoneCurry":
            self.PhoneCurryCall()


    def AmazonCall(self):
        query = self.brand + " " + self.model + " " + "product-reviews Amazon india"
        amazon = AmazonClass(self.brand, self.model)
        amazon.seachByName(query, self.pages)

    def FlipkartCall(self):
        query = self.brand + " " + self.model + " flipkart product reviews"
        flipkart = Flipkart(self.brand, self.model)
        # t = Thread(target=flipkart.searchByName, args=(query, self.pages,))
        # t.start()
        # t.join()
        print("2. CALLING SEARCH BY NAME")
        flipkart.searchByName(query, self.pages)

    def SmartprixCall(self):
        query = self.brand + " " + self.model + " smartprix"
        smartprix = SmartPrix()
        smartprix.searchByName(query, self.brand, self.model)

    def Mobiles91Call(self):
        query = self.brand + " " + self.model + " 91mobiles hub review"
        mobiles91 = Mobiles91()
        mobiles91.searchByName(query, self.brand, self.model)

    def IndiaTodayCall(self):
        query = self.brand + " " + self.model + " review india today group"
        indiatoday = IndiaToday()
        indiatoday.seacrchByName(query, self.brand, self.model)

    def PhoneCurryCall(self):
        query = self.brand + " " + self.model + " phonecurry"
        phonecurry = PhoneCurry()
        phonecurry.searchByName(query, self.brand, self.model)

    def getSelection(self):
        self.brand = self.variable1.get()
        print("Brand : ",  self.brand)

    def analyseByURL(self):
        print("####################################################")
        print("####################################################")
        print("\n")
        self.model = str(self.entry_model.get())
        print(self.model)

        self.brand = self.variable1.get()
        print("Brand : ", self.brand)

        self.website = self.variable2.get()
        print("Website : ", self.website)

        self.pages = int(self.entry_pages.get())
        print("Pages : ", self.pages)

        url = str(self.entry_url.get())

        if self.website == "Amazon":
            amz = AmazonClass(self.brand, self.model)
            amz.searchByUrl(url, self.pages)

        elif self.website == "Flipkart":
            fp = Flipkart(self.brand, self.model)
            fp.seachByUrl(url, self.pages)

        elif self.website == "SmartPrix":
            sm = SmartPrix()
            sm.searchByURL(url, self.brand, self.model)

        elif self.website == "91mobiles":
            mo = Mobiles91()
            mo.searchByURL(url, self.brand, self.model)

        elif self.website == "IndiaToday":
            ind = IndiaToday()
            ind.searchByURL(url, self.brand, self.model)

        elif self.website == "PhoneCurry":
            pc = PhoneCurry()
            pc.searchByURL(url, self.brand, self.model)



    def AnalyseReport(self):
        fwa = featurewiseanalysis(self.fileName, "Analysis")
        self.features = []
        self.all_list = []
        self.pos_list = []
        self.neg_list = []
        if self.camera_var.get() == 1:
            all_count, positive_count, negative_count = fwa.calculatePolarity("camera")
            self.features.append("Camera")
            self.all_list.append(all_count)
            self.pos_list.append(positive_count)
            self.neg_list.append(negative_count)
            print("Camera")
        if self.battery_var.get() == 1:
            all_count, positive_count, negative_count = fwa.calculatePolarity("battery")
            self.features.append("Battery")
            self.all_list.append(all_count)
            self.pos_list.append(positive_count)
            self.neg_list.append(negative_count)
            print("Battery")
        if self.finger_var.get() == 1:
            all_count, positive_count, negative_count = fwa.calculatePolarity("finger")
            self.features.append("Finger Print")
            self.all_list.append(all_count)
            self.pos_list.append(positive_count)
            self.neg_list.append(negative_count)
            print("Finger Print")
        if self.display_var.get() == 1:
            all_count, positive_count, negative_count = fwa.calculatePolarity("display")
            self.features.append("Display")
            self.all_list.append(all_count)
            self.pos_list.append(positive_count)
            self.neg_list.append(negative_count)
            print("Display")

        print("Features List : ", self.features)
        print("All List : ", self.all_list)
        print("Pos List : ", self.pos_list)
        print("Neg List : ", self.neg_list)

    def PrintResults(self):
        print(self.option.get())
        selected_value = str(self.option.get())
        index = self.features.index(selected_value)
        total_count = self.all_list[index]
        pos_count = self.pos_list[index]
        neg_count = self.neg_list[index]
        pos_percentage = round((int(pos_count) / int(total_count)) * 100, 2)
        neg_percentage = round((int(neg_count) / int(total_count)) * 100, 2)

        all_text = selected_value + " Total Apperared = " + str(total_count)
        pos_text = "Positive Count = " + str(pos_count) + " , Percentage = " + str(pos_percentage) + "%"
        neg_text = "Negative Count = " + str(neg_count) + " , Percentage = " + str(neg_percentage) + "%"


        # label_ftr = Label(self.master, text=selected_value, padx=10, pady=10).grid(row=11, column=0)
        label_all = Label(self.frame4, text=all_text, padx=10, pady=10).grid(row=13, column=0, sticky=W)
        label_pos = Label(self.frame4, text=pos_text, padx=10, pady=10).grid(row=14, column=0, sticky=W)
        lable_neg = Label(self.frame4, text=neg_text, padx=10, pady=10).grid(row=15, column=0, sticky=W)

    def openExcelFile(self):
        if self.website=='Amazon' or self.website=='Flipkart':
            self.fileName = "Reviews_" + self.brand + "_" + self.model + ".xlsx"
            os.startfile("UserReviewsData.xlsx")
            os.startfile(self.fileName)
        elif self.website=="ALL":
            os.startfile("UserReviewsData.xlsx")
            os.startfile("CriticsData.xlsx")
        else:
            os.startfile("CriticsData.xlsx")

    def getComments(self):
        feature = str(self.variable3.get()).lower()
        category = str(self.variable4.get())
        print(feature)
        print(category)

        control = Controller(self.fileName, "Analysis", feature, category)
        self.all_comments = control.getResults()

        self.numberOfComments = len(self.all_comments)

        self.comment_text.delete("1.0", "end")
        self.index = 0
        self.comment_text.insert(END, self.all_comments[0])

    def onNextClick(self):
        if self.index == self.numberOfComments-1:
            pass
        else:
            self.index += 1
            self.comment_text.delete("1.0", END)
            # print(self.all_comments[self.index])
            self.comment_text.insert(END, self.all_comments[self.index])

    def onPervClick(self):
        if self.index == 0:
            pass
        else:
            self.index -= 1
            self.comment_text.delete("1.0", END)
            # print(self.all_comments[self.index])
            self.comment_text.insert(END, self.all_comments[self.index])


root = Tk()
root.geometry('1500x900')
InterFace(root)
root.mainloop()

# https://stackoverflow.com/questions/46209627/nesting-grids-and-frames-in-tkinter-and-python