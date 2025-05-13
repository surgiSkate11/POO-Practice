from django.forms import ModelForm, TextInput, EmailInput, NumberInput, Select
from django import forms
from .models import Empleado, Cargo, Departamento, TipoContrato, Rol


class EmpleadoForm(ModelForm):
    # Definir las opciones para el combobox de cargos
    # CARGO_CHOICES = [
    #     ('', 'Seleccione un cargo'),
    #     ('Médico General', 'Médico General'),
    #     ('Cardiólogo', 'Cardiólogo'),
    #     ('Dermatólogo', 'Dermatólogo'),
    #     ('Neurólogo', 'Neurólogo'),
    #     ('Pediatra', 'Pediatra'),
    #     ('Ginecólogo', 'Ginecólogo'),
    #     ('Oftalmólogo', 'Oftalmólogo'),
    #     ('Traumatólogo', 'Traumatólogo'),
    #     ('Psiquiatra', 'Psiquiatra'),
    #     ('Odontólogo', 'Odontólogo'),
    # ]

    # # Sobreescribir el campo cargo para convertirlo en un select
    # # Esto reemplaza el campo CharField del modelo con un campo de selección en el formulario
    # cargo = forms.ChoiceField(
    #     choices = CARGO_CHOICES,
    #     widget=forms.Select(attrs={'class': 'form-control'})
    # )
    class Meta:
        model = Empleado
        # fields = ['name',' email','phone','cargo']
        #cada campo lo convierte a un control html <input type="text" name="name" id="name" class="form-control" placeholder="Nombre del empleado" required>
        fields = '__all__'
        # exclude = ['phone']

        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del empleado', 'required': 'required'}),
            'cedula': TextInput(attrs={'class': 'form-control', 'placeholder': 'Cédula', 'required': 'required'}),
            'cargo': Select(attrs={'class': 'form-control', 'placeholder': 'Cargo', 'required': 'required'}),
            'direccion': TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección', 'required': 'required'}),
            'sexo': Select(attrs={'class': 'form-control', 'placeholder': 'Sexo', 'required': 'required'}),
            'sueldo': TextInput(attrs={'class': 'form-control', 'placeholder': 'Sueldo', 'required': 'required'}),
            'departamento': Select(attrs={'class': 'form-control', 'placeholder': 'Departamento', 'required': 'required'}),
            'tipo_contrato': Select(attrs={'class': 'form-control', 'placeholder': 'Tipo de contrato', 'required': 'required'}),
        }

class CargoForm(ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'
        widgets = {
            'descripcion': TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripción', 'required': 'required'}),
        }
class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'
        widgets = {
            'descripcion': TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripción', 'required': 'required'}),
        }

class ContratoForm(ModelForm):
    class Meta:
        model = TipoContrato
        fields = '__all__'
        widgets = {
            'descripcion': TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripción', 'required': 'required'}),
        }

class RolForm(ModelForm):
    class Meta:
        model = Rol
        fields = ['empleado', 'aniomes', 'sueldo', 'horas_extra', 'bono']
        # exclude = ['iess', 'tot_ing', 'tot_des', 'neto']
        # Esto es para que no se muestren los campos iess, tot_ing, tot_des y neto en el formulario
        # ya que estos se calculan automáticamente en el modelo
        widgets = {
            'empleado': Select(attrs={'class': 'form-control'}),
            'aniomes': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'sueldo': forms.NumberInput(attrs={'class': 'form-control'}),
            'horas_extra': forms.NumberInput(attrs={'class': 'form-control'}),
            'bono': forms.NumberInput(attrs={'class': 'form-control'}),
        }
