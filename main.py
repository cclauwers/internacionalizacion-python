from persona import Persona
import gettext


idiomas = ['en','nl_BE']
t = gettext.translation('main', localedir='locales', languages=idiomas ,fallback=True,)
t.install()

_ = t.gettext


numCuentas = 2
clientes = []
opcion = 0

persona0 = Persona('Cindy', 'ccc', 3.0, 0)
persona1 = Persona('Marc', 'gt', 100.0, 1)
clientes.append(persona0)
clientes.append(persona1)

while 6 != opcion:
    opcion = input(_('''Por favor seleccione una operacion:
    1 Ver cuentas
    2 Crear cuenta
    3 Ver saldo
    4 Hacer ingreso
    5 Hacer retirada
    6 Exit
    '''))

    if(opcion == 1):

        for cliente in clientes:
            print(_('Nombre: ') + cliente.getNombre())
            print(_('Apellido: ') + cliente.getApellido())
            print(_('Numero de Cuenta: ') + str(cliente.getNumeroCuenta()))
            print('\n')
        raw_input(_("Pulse Enter para continuar..."))
    elif(opcion == 2) :
        nombre = input(_('Introduzca nombre: '))
        apellido = input(_('Introduzca apellido: '))

        persona = Persona(nombre, apellido, 0.0, numCuentas)
        numCuentas += 1
        clientes.append(persona)
        print(_("Cuenta creada"))
        raw_input(_("Pulse Enter para continuar..."))

    elif(opcion == 3) :
        cuenta = input(_('Por favor indique el numero de cuenta:'))
        print(_('El saldo de la cuenta ' +str(cuenta)+' es de: '+ str(clientes[int(cuenta)].getSaldo()) + ' Euros'))
        raw_input(_('Pulse Enter para continuar...'))

    elif(opcion == 4) :
        cuenta = input(_('Por favor indique el numero de cuenta al que desea hacer el ingreso:'))
        cantidad = input(_('Por favor indique la cantidad a ingresar:'))
        clientes[int(cuenta)].hacerIngreso(int(cantidad))
        print(_('Se ha realizado el ingreso'))
        raw_input(_("Pulse Enter para continuar..."))

    elif(opcion == 5):
        cuenta = input(_('Por favor indique el numero de cuenta al que desea hacer el ingreso:'))
        cantidad = input(_('Por favor indique la cantidad a retirar:'))
        clientes[int(cuenta)].retirarDinero(int(cantidad))
        print(_('Se ha realizado la retirada'))
        raw_input(_("Pulse Enter para continuar..."))


print(_('Fin del programa'))
