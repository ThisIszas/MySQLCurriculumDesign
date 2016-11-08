# coding:utf-8
# http://blog.csdn.net/chenghit/article/details/50421090
# http://www.cnblogs.com/dyx1024/archive/2012/07/05/2578579.html
import wx


class RebuildFrame(wx.Frame):  # 主框体,所有界面都往Frame里加
    def __init__(self, *args, **kwargs):
        super(RebuildFrame, self).__init__(*args, **kwargs)
        self.CreateStatusBar()
        filemenu = wx.Menu()

        filemenu.Append(wx.ID_ABOUT, "&About", " Information about this program.")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT, "&Save", " Save information.")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT, "&Exit", " Terminate the program.")

        menu_bar = wx.MenuBar()
        menu_bar.Append(filemenu, "&File")
        self.SetMenuBar(menu_bar)

        notebook = wx.Notebook(self)
        self.login_form = LoginForm(notebook)
        notebook.AddPage(self.login_form, 'Login Page')
        self.SetClientSize((830, 400))  # (宽, 高)
        self.Show()


class LoginForm(wx.Panel):  #登录界面
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.login_name_Label = ""
        self.confirm_button = ""
        self.username_label = ""
        self.password = ""
        self.nameTextCtrl = ""
        self.passwordTextCtrl = ""
        self.create_controls()
        self.do_layout()

    def create_controls(self):
        self.login_name_Label = wx.StaticText(self, label=u"学生成绩管理系统")
        self.confirm_button = wx.Button(self, label=u"登录")
        self.username_label = wx.StaticText(self, label=u"用户名")
        self.password = wx.StaticText(self, label=u"密码")
        self.nameTextCtrl = wx.TextCtrl(self, value="")
        self.passwordTextCtrl = wx.TextCtrl(self, value=u"", style=wx.TE_PASSWORD)

    def do_layout(self):
        for control, x, y, width, height in \
                [(self.login_name_Label, 360, 90, -1, -1),
                 (self.username_label, 290, 150, -1, -1),
                 (self.nameTextCtrl, 330, 148, 150, 25),
                 (self.password, 295, 183, -1, -1),
                 (self.passwordTextCtrl, 330, 178, 150, 25),
                 (self.confirm_button, 350, 210, -1, -1)
                 ]:
            control.SetDimensions(x=x, y=y, width=width, height=height)


app = wx.App(False)
frame = RebuildFrame(None, title=u'学生数据库管理系统')
app.MainLoop()
