from django.shortcuts import render, redirect, get_object_or_404 
from .models import Persona
from .forms import PersonaForm

# --- VISTA PARA REGISTRAR ---
def registrar_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reporte_personas')
    else:
        form = PersonaForm()
    
    # Título dinámico al contexto
    context = {
        'form': form,
        'titulo': 'Registro de Datos Personales'
    }
    return render(request, 'registrar_persona.html', context)

# --- VISTA PARA LISTAR (REPORTE) ---
def reporte_personas(request):
    personas = Persona.objects.all().order_by('apellidos', 'nombres')
    return render(request, 'reporte_personas.html', {'personas': personas})

# --- VISTA PARA EDITAR ---
def editar_persona(request, pk):
    # Busca la persona por su ID (pk). Si no existe, devuelve error 404.
    persona = get_object_or_404(Persona, pk=pk)
    
    if request.method == 'POST':
        # 'instance=persona' carga los datos previos para que se actualicen en vez de crear uno nuevo
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('reporte_personas')
    else:
        # Carga el formulario con los datos actuales de la persona
        form = PersonaForm(instance=persona)

    context = {
        'form': form,
        'titulo': f'Editando a: {persona.nombres} {persona.apellidos}'
    }
    return render(request, 'registrar_persona.html', context)

# --- VISTA PARA ELIMINAR ---
def eliminar_persona(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    
    if request.method == 'POST':
        persona.delete()
        return redirect('reporte_personas')
    
    return redirect('reporte_personas')
