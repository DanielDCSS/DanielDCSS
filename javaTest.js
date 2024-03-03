/* var carro = {
    cor: 'Vermelho',
    machas: true,
    relaPos: 40,
    relaTemp: 20,
    vEscMed: function() {
        return this.relaPos/this.relaTemp;
    }
}
var moto = new Object() ;
moto.cor = 'cinza';
moto.machas = false;
moto.relaPos = 50;
moto.relaTemp = 25;
moto.vEscMed =  function() {
    return this.relaPos/this.relaTemp;
} */
function Auto(cor, machas, relaPos, relaTemp, vEscMed) {
    this.cor = cor ;
    this.machas = machas ;
    this.relaPos = relaPos ;
    this.relaTemp = relaTemp ;
    this.vEscMed = function() {
        return this.relaPos/this.relaTemp;
    };
}
function finalArry(obj) {
    v = [obj.cor, obj.machas, obj.relaPos, obj.relaTemp, obj.vEscMed()];
    return v ;
}
var carro = new Auto('Vermelho', true, 40, 20);
var moto = new Auto('Cinza', false, 50, 25);
console.log(finalArry(carro), finalArry(moto));
