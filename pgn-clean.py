import os
import psutil
import shutil
import tkinter as tk
from tkinter import filedialog, Toplevel, Label, Button, StringVar
from tkinter.ttk import Progressbar

def kill_process_if_running(process_name):
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if proc.info['name'] == process_name:
            proc.kill()

kill_process_if_running('analyse.exe')

def check_and_create_folders():
    output_folder = 'OUTPUT'
    tools_folder = 'TOOLS'
    folders = ['CLEANED', 'DUPES', 'ORIG_UNCLEANED', 'STATS']
    
    for folder in folders:
        path = os.path.join(output_folder, folder)
        if not os.path.exists(path):
            os.makedirs(path)
    
    if not os.path.exists(tools_folder):
        os.makedirs(tools_folder)

def copy_pgn_file():
    for filename in os.listdir('.'):
        if filename.endswith('.pgn'):
            shutil.copy(filename, os.path.join('OUTPUT', 'ORIG_UNCLEANED', filename))

def delete_unwanted_files():
    unwanted_files = [
        'ecodb.pgn', 'manifest-f', 'outPlies', 'outRes', '1.pgn', 'outR.pgn', 
        'outfile1.pgn', 'unique1.pgn', 'unique2.pgn', 'out7.pgn', 'out3.pgn', 
        'outX.pgn', 'out2.pgn', 'outRes2', 'outRes3', 'resultlist.txt', 
        'dupes.txt', 'outSummary', 'outName', 'outName3', 'outName2', 
        'nameList.txt', 'out4.pgn', 'clusterlist.txt', 'outCluster2', 
        'outColor', 'colorlist.txt', 'outEco', 'ecolist.txt', 'resW.pgn', 
        'white_wins.pgn', 'resD.pgn', 'draws.pgn', 'resB.pgn', 'black_wins.pgn', 
        'resN.pgn', 'no_result.pgn', 'out4.analyzed.pgn', 'analyzed.pgn', 
        'out4.stats.txt', 'analyzed.stats.txt'
    ]
    for filename in os.listdir('.'):
        if os.path.isfile(filename) and (filename in unwanted_files or filename.endswith('.pgi')):
            os.remove(filename)

def clear_output_directories():
    output_dirs = ['OUTPUT/CLEANED', 'OUTPUT/DUPES', 'OUTPUT/STATS']
    for dir in output_dirs:
        for filename in os.listdir(dir):
            file_path = os.path.join(dir, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("PGN files", "*.pgn")])
    if file_path:
        progress_window = Toplevel(app)
        progress_window.title("Loading PGN File")
        progress_window.geometry("300x100")
        progress_label = Label(progress_window, text="Loading file, please wait...", padx=10, pady=10)
        progress_label.pack()
        progress_bar = Progressbar(progress_window, orient="horizontal", length=250, mode="indeterminate")
        progress_bar.pack(pady=20)
        progress_bar.start()

        app.update_idletasks()
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
        with open(os.path.basename(file_path), 'w', encoding='utf-8') as new_file:
            new_file.write(content)

        progress_bar.stop()
        progress_window.destroy()
        show_popup()

def show_popup():
    popup = Toplevel(app)
    popup.title("Notification")
    popup.geometry("200x100")
    label = Label(popup, text="PGN Loaded!", padx=10, pady=10)
    label.pack()
    button = Button(popup, text="OK", command=popup.destroy)
    button.pack(pady=10)

def run_batch_file():
    if remove_duplicates_var.get() == '0' and create_extra_stats_var.get() == '0' and create_extra_stats_analysis_var.get() == '0':
        os.startfile(r'TOOLS\process.bat')
        
    elif remove_duplicates_var.get() == '0' and create_extra_stats_var.get() == '1' and create_extra_stats_analysis_var.get() == '0':
        os.startfile(r'TOOLS\process2.bat')
        
    elif remove_duplicates_var.get() == '0' and create_extra_stats_var.get() == '1' and create_extra_stats_analysis_var.get() == '1':
        os.startfile(r'TOOLS\process3.bat')
   
    elif remove_duplicates_var.get() == '0' and create_extra_stats_var.get() == '0' and create_extra_stats_analysis_var.get() == '1':
        os.startfile(r'TOOLS\process3.bat')
        
    elif remove_duplicates_var.get() == '1' and create_extra_stats_var.get() == '0' and create_extra_stats_analysis_var.get() == '0':
        os.startfile(r'TOOLS\process4.bat')
        
    elif remove_duplicates_var.get() == '1' and create_extra_stats_var.get() == '1' and create_extra_stats_analysis_var.get() == '0':
        os.startfile(r'TOOLS\process5.bat')
   
    elif remove_duplicates_var.get() == '1' and create_extra_stats_var.get() == '1' and create_extra_stats_analysis_var.get() == '1':
        os.startfile(r'TOOLS\process6.bat')
        
    elif remove_duplicates_var.get() == '1' and create_extra_stats_var.get() == '0' and create_extra_stats_analysis_var.get() == '1':
        os.startfile(r'TOOLS\process6.bat')

def open_info_window():
    info_window = Toplevel(app)
    info_window.title("Information")
    info_window.configure(bg='darkgrey')
    info_text = (
        "                   PGN-Clean by Jim Ablett\n"
        "                   ------------------------------------\n\n"
        "To clean/normalize and process a pgn file >\n"
        "These are the steps which are done automatically.\n\n"
        "--------------------------   CLEAN   ------------------------\n\n"
        "Step  1:  Backup original pgn file.\n"
        "Step  2: 'Trim'             to correctly re-format pgn file.\n"
        "Step  3: 'PgnMan'       to remove duplicates\n"
        "Step  4: 'Joined'          to remove errors.\n"
        "Step  5: 'Pgn-Extract'  to fix errors.\n" 
        "Step  6: 'tagFix'          to fix tag errors.\n"
        "Step  7: 'tagOrder'       to put tags in the correct order.\n"
        "Step  8: 'plyCount'       to add ply count tag.\n"
        "Step  9: 'cleanUp'        to fix errors in the tag section.\n"
        "Step 10: 'PgnMan'       to add ECO to openings.\n"
        "Step 11: 'gameNum'   inserts consecutive 'game numbers'.\n\n"
        "--------------------------   STATS   --------------------------\n\n"
        "Step 12: 'resultList'   to produce a crosstable of games.\n"
        "Step 13: 'Summary'   to produce a summary stats file.\n\n"
        
        "------  If  'Create Extra Stats'  checkbox is ticked   ------\n\n"
        "Step 14: 'Ordo'          to produce an ELO ratings list.\n"
        "Step 15: 'NameList'   to produce player stats file.\n"
        "Step 16: 'clusterList'  to list player clusters.\n"
        "Step 17: 'colorList'     to list player results by colour.\n"
        "Step 18: 'EcoList'      to produce an ECO stats file.\n"
        "Step 19: 'resultSplit'  to produce PGNs based on results.\n\n"
        "--- If  'Create Extra Stats + Analysis PGN'  checkbox is ticked  ---\n\n"
        "Step 20: 'Apgn'  to produce an analysis PGN and stats.\n\n"     
        "Processed files will be found in the 'OUTPUT' folder.\n"
    )
    label = Label(info_window, text=info_text, bg='darkgrey', fg='black', font=('Arial', 10), justify='left')
    label.pack(padx=10, pady=10)

app = tk.Tk()
app.title("PGN-Clean")
app.configure(bg='darkgrey')

delete_unwanted_files()
clear_output_directories()
check_and_create_folders()
copy_pgn_file()

remove_duplicates_var = StringVar(value='0')
remove_duplicates_checkbox = tk.Checkbutton(app, text='Remove duplicates', variable=remove_duplicates_var, onvalue='1', offvalue='0', bg='darkgrey', fg='black', font=('Arial', 10))
remove_duplicates_checkbox.pack(pady=10)

create_extra_stats_var = StringVar(value='0')
create_extra_stats_checkbox = tk.Checkbutton(app, text='Create Extra Stats', variable=create_extra_stats_var, onvalue='1', offvalue='0', bg='darkgrey', fg='black', font=('Arial', 10))
create_extra_stats_checkbox.pack(pady=10)

create_extra_stats_analysis_var = StringVar(value='0')
create_extra_stats_analysis_checkbox = tk.Checkbutton(app, text='Stats/Analyze/Annotate PGN (very small pgns best)', variable=create_extra_stats_analysis_var, onvalue='1', offvalue='0', bg='darkgrey', fg='black', font=('Arial', 10))
create_extra_stats_analysis_checkbox.pack(pady=10)

info_label = tk.Label(app, text="A utility to automatically clean & correct errors in\nPGN files using PGN-Extract by David J Barnes, 40-H tools\n by Norman Pollock, Joined by Andreas Stabel,\n PGN Manager by Eduardo Suastegui, Analyse-PGN\nby Jubal Mordecai Velasco & Ordo by Miguel A. Ballicora",bg='darkgrey', fg='black', font=('Arial', 10))
info_label.pack(pady=10)

load_button = tk.Button(app, text="Load PGN File", command=load_file, bg='grey', fg='white', font=('Arial', 12))
load_button.pack(pady=10)

run_button = tk.Button(app, text="Process PGN", command=run_batch_file, bg='green', fg='white', font=('Arial', 12))
run_button.pack(pady=10)

info_button = tk.Button(app, text="Info", command=open_info_window, bg='blue', fg='white', font=('Arial', 12))
info_button.pack(pady=10)

app.update_idletasks()
app_width = app.winfo_reqwidth()
app_height = app.winfo_reqheight()
app.geometry(f"{app_width}x{app_height}+100+100")

app.mainloop()

