import os
from subprocess import call

##packages = [dist.project_name for dist in pip.get_installed_distributions()]
##print ("pip3 install --upgrade " + ' '.join(packages))


packages = "pdf-table-extract networkx scikit-image pywavelets pytesseract XlsxWriter WMI web.py traitlets tornado six singledispatch setuptools selenium scipy scikit-learn pyzmq pywin32 pytz PyTweening python-docx python-dateutil PyScreeze pypiwin32 pyperclip PyPDF2 pyPdf pyparsing PyMsgBox PyInstaller pyHook pygame pycairo PyAutoGUI py2exe psutil pip Pillow pdfminer pandas openpyxl numpy nltk matplotlib lxml lpthw.web jupyter-core jupyter-client jdcal iterutils ipython-genutils imutils functools32 et-xmlfile enum34 easygui docx Django decorator cycler certifi backports-abc pyrsvg pygtksourceview pygtk pygoocanvas pygobject"

packages = packages.split(' ')

install_Command = 'pip2 install --trusted-host pypi.python.org'
count = 0

for package in packages:
    #print (package)
    install_Command = install_Command + ' ' + package
    
    if count % 5 == 0:
        print (install_Command)
        #print (os.system(install_Command))
        install_Command = 'pip2 install --trusted-host pypi.python.org'

    count = count + 1
    


#pip install --upgrade pdf-table-extract networkx scikit-image pywavelets pytesseract XlsxWriter WMI web.py traitlets tornado six singledispatch setuptools selenium scipy scikit-learn pyzmq pywin32 pytz PyTweening python-docx python-dateutil PyScreeze pypiwin32 pyperclip PyPDF2 pyPdf pyparsing PyMsgBox PyInstaller pyHook pygame pycairo PyAutoGUI py2exe psutil pip Pillow pdfminer pandas openpyxl numpy nltk matplotlib lxml lpthw.web jupyter-core jupyter-client jdcal iterutils ipython-genutils imutils functools32 et-xmlfile enum34 easygui docx Django decorator cycler certifi backports-abc pyrsvg pygtksourceview pygtk pygoocanvas pygobject



#pip3 install --upgrade zodbpickle widgetsnbextension wheel Werkzeug wcwidth traitlets tornado testpath tensorflow tensorflow-tensorboard sklearn simplegeneric setuptools scipy scikit-misc scikit-learn scikit-image qtconsole pyzmq PyYAML PyWavelets pytz python-mnist python-dateutil pytest pyparsing Pygments pygit2 pygame pycparser py protobuf prompt-toolkit pluggy pip Pillow pickleshare parso pandocfilters pandas opencv-python numpy notebook networkx nbformat nbconvert mistune matplotlib MarkupSafe Markdown Keras jupyter jupyter-core jupyter-console jupyter-client jsonschema Jinja2 jedi ipywidgets ipython ipython-genutils ipykernel html5lib h5py enum34 entrypoints decorator Cython cycler colorama cffi bleach attrs pyopenssl six
