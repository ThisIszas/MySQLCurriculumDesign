#Boa:Frame:Frame1
#coding=utf-8


import wx


def create(parent):
    return Frame1(parent)


[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON5, wxID_FRAME1BUTTON6,
wxID_FRAME1PANEL1, wxID_FRAME1PANEL2, wxID_FRAME1STATICTEXT1,
] = [wx.NewId() for _init_ctrls in range(7)]


class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='Frame1', parent=prnt,
        pos=wx.Point(660, 303), size=wx.Size(420, 265),
        style=wx.DEFAULT_FRAME_STYLE, title='\xcb\xc4\xbc\xbe')
        self.SetClientSize(wx.Size(412, 231))
        print '\xcb\xc4'.decode('gbk')

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
        pos=wx.Point(0, 0), size=wx.Size(412, 231),
        style=wx.TAB_TRAVERSAL)


        self.panel2 = wx.Panel(id=wxID_FRAME1PANEL2, name='panel2', parent=self,
        pos=wx.Point(0, 0), size=wx.Size(412, 231),
        style=wx.TAB_TRAVERSAL)
        self.panel2.Show(False)


        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label='\xb4\xba',
        name='button1', parent=self.panel1, pos=wx.Point(30, 30),
        size=wx.Size(75, 25), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
        id=wxID_FRAME1BUTTON1)
        print '\xb4\xba'.decode('gbk')

        self.button5 = wx.Button(id=wxID_FRAME1BUTTON5,
        label='\xcd\xcb\xb3\xf6', name='button5', parent=self.panel1,
        pos=wx.Point(120, 80), size=wx.Size(75, 25), style=0)
        self.button5.Bind(wx.EVT_BUTTON, self.OnButton5Button,
        id=wxID_FRAME1BUTTON5)


        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
        label='\xb4\xba', name='staticText1', parent=self.panel2,
        pos=wx.Point(178, 86), size=wx.Size(56, 59), style=0)
        self.staticText1.Center(wx.BOTH)
        self.staticText1.SetFont(wx.Font(42, wx.SWISS, wx.NORMAL, wx.NORMAL,
        False, '\xbb\xaa\xce\xc4\xd0\xd0\xbf\xac'))
        self.staticText1.SetForegroundColour(wx.Colour(0, 128, 0))
        self.staticText1.Show(False)


        self.button6 = wx.Button(id=wxID_FRAME1BUTTON6,
        label='\xb7\xb5\xbb\xd8', name='button6', parent=self.panel2,
        pos=wx.Point(304, 168), size=wx.Size(75, 24), style=0)
        self.button6.Show(False)
        self.button6.Bind(wx.EVT_BUTTON, self.OnButton6Button,
        id=wxID_FRAME1BUTTON6)

    def __init__(self, parent):
        self._init_ctrls(parent)

    # 对panel1的button定义功能
    def OnButton1Button(self, event):
        self.panel1.Show(False)
        self.panel2.Show(True)
        #self.staticText1.Show(True)
        #self.button6.Show(True)

    def OnButton5Button(self, event):
        self.Close()

    # 对其他panel的button定义功能
    def OnButton6Button(self, event):
        self.panel2.Show(False)
        self.panel1.Show(True)
        #self.staticText1.Show(False)
        #self.button6.Show(False)

app=wx.App()
frame=Frame1(None)
frame.Show()
app.MainLoop()
