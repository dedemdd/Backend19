import { restar} from './2_funciones';


//Si una variable va a cambiar mas de una vez, entonces no se usa const sino let
const x = 'Denys'

x = 'ramiro'
x = 'Juan'
x = 20
console.log('Hola')

function sumar(numero1, numero2) {
    const resultado = numero1 + numero2

    return resultado
}

const sumatoria = sumar(10, 10)

console.log(sumatoria)

const resta = restar(50,30)
console.log(resta)