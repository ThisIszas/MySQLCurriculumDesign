# coding:utf-8
import wx


class RebuildFrame(wx.Frame):
    def __init__(self, parent, title, size):
        wx.Frame.__init__(self, parent, title=title, size=size)
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
        form1 = LoginForm(notebook)
        notebook.AddPage(form1, 'Login Page')
        self.SetClientSize(notebook.GetBestSize())
        self.Show()


class LoginForm(wx.Panel):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.login_name_Label = ""
        self.confirm_button = ""
        self.username_label = ""
        self.password = ""
        self.nameTextCtrl = ""
        self.passwordTextCtrl = ""
        self.create_controls()
    #    self.do_layout()

    def create_controls(self):
        self.login_name_Label = wx.StaticText(self, label=u"学生成绩管理系统")
        self.confirm_button = wx.Button(self, label=u"确认")
        self.username_label = wx.StaticText(self, label=u"用户名")
        self.password = wx.StaticText(self, label=u"密码")
        self.nameTextCtrl = wx.TextCtrl(self, value="")
        self.passwordTextCtrl = wx.TextCtrl(self, value=u"", style=wx.TE_PASSWORD)

    # def do_layout(self):
    #     raise NotImplementedError


class DoLayout1(LoginForm):
    def do_layout(self):
        box_sizer = wx.BoxSizer(orient=wx.HORIZONTAL)
        grid_sizer = wx.FlexGridSizer(rows=5, cols=2, vgap=10, hgap=10)
        expand_option = dict(flag=wx.EXPAND)
        no_options = dict()
        empty_space = ((0, 0), no_options)

        for control, options in\
            [(self.login_name_Label, dict(flag=wx.ALIGN_CENTER)),
             (self.nameTextCtrl, expand_option),
             (self.password, no_options),
             (self.passwordTextCtrl, expand_option),
             empty_space,
             (self.confirm_button, expand_option),
             empty_space,
             (self.confirm_button, dict(flag=wx.ALIGN_CENTER))]:
            grid_sizer.Add(control, **options)

        for control, options in \
                [(grid_sizer, dict(border=5, flag=wx.ALL)),
                 (self.logger, dict(border=5, flag=wx.ALL | wx.EXPAND, proportion=1))]:
            box_sizer.Add(control, **options)
        self.SetSizerAndFit(box_sizer)

app = wx.App(False)
frame = RebuildFrame(None, u"测试版SQLGUI", (888, 888))
# panel = BasePanel(frame)
# frame.Show()
app.MainLoop()