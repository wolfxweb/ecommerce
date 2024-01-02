
function consultarCEP() {
    var cep = document.getElementById('id_cep').value;
    cep = cep.replace(/\D/g, '');

    if (cep.length !== 8) {
        alert('CEP inválido. Por favor, insira um CEP válido.');
        return;
    }

    var url = 'https://viacep.com.br/ws/' + cep + '/json/';

    fetch(url)
        .then(response => response.json())
        .then(data => {
           
            let idEnderecoCampo = document.getElementById('id_endereco');
            idEnderecoCampo.value = data.logradouro;
            let id_bairro = document.getElementById('id_bairro');
            id_bairro.value = data.bairro;
            let id_cidade = document.getElementById('id_cidade');
            id_cidade.value = data.localidade;
            let id_estado = document.getElementById('id_estado');
            id_estado.value = data.uf;
        })
        .catch(error => {
            console.error('Erro ao consultar CEP:', error);
            alert('Erro ao consultar CEP. Por favor, tente novamente.');
        });
}
