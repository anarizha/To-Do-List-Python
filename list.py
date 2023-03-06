import PySimpleGUI as sg

def adicionar_tarefa(tarefa, tarefas):
    if tarefa != '':
        tarefas.append(tarefa)
    return tarefas

def remover_tarefa(tarefa, tarefas):
    if tarefa in tarefas:
        tarefas.remove(tarefa)
    return tarefas

tarefas = []

sg.theme('LightBlue')  # definindo o tema

layout = [
    [sg.Text("Digite uma tarefa:")],
    [sg.InputText(key="-TAREFA-")],
    [sg.Button("Adicionar", key="-ADICIONAR-", button_color=('white', '#778899')), 
     sg.Button("Remover", key="-REMOVER-", button_color=('white', '#778899')), 
     sg.Button("Sair", key="-SAIR-", button_color=('white', '#778899'))],
    [sg.HorizontalSeparator()],
    [sg.Text('', font=('Arial', 10), background_color='#89CFF0', pad=(0,10), size=(4, 1))],
    [sg.Listbox(values=tarefas, size=(40, 10), key="-LIST-", background_color='#F5F5F5')]
]

window = sg.Window("Lista de Tarefas", layout, background_color='#89CFF0', resizable=True, size=(400, 400))  # definindo a cor de fundo e o tamanho da janela

while True:
    event, values = window.read()
    
    if event == "-ADICIONAR-":
        tarefas = adicionar_tarefa(values["-TAREFA-"], tarefas)
        window['-LIST-'].update(tarefas)
        window['-TAREFA-'].update('')
    
    elif event == "-REMOVER-":
        tarefas = remover_tarefa(values["-LIST-"][0], tarefas)
        window['-LIST-'].update(tarefas)
    
    elif event == "-SAIR-" or event == sg.WIN_CLOSED:
        break

window.close()
