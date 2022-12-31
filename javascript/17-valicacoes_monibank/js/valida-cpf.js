export default function ehUmCPF(campo) {
    const cpf = campo.value.replace(/\.|-/g, "");
    if (validaNumerosRepetidos(cpf) || validaDigito(cpf, 10, 9) || validaDigito(cpf, 11, 10)) {
        campo.setCustomValidity('Esse CPF não é válido');
    } else {
        console.log("Existe")
    }
}


function validaNumerosRepetidos(cpf) {
    const numerosRepetidos = [
        '00000000000',
        '11111111111',
        '22222222222',
        '33333333333',
        '44444444444',
        '55555555555',
        '66666666666',
        '77777777777',
        '88888888888',
        '99999999999'
    ]

    return numerosRepetidos.includes(cpf);
}


function validaDigito(cpf, mult, tam) {
    let soma = 0;
    let multiplicador = mult;

    for (let tamanho = 0; tamanho < tam; tamanho++) {
        soma += cpf[tamanho] * multiplicador;
        multiplicador--;
    }

    soma = (soma*10) % 11;

    if (soma==10 || soma==1) {
        soma = 0;
    }

    return soma != cpf[tam];
}
