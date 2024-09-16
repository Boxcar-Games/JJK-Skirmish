function yuji(Health, Attack, Defense, Speed, cursedEnergy) {
  this.Health = 200;
  this.Attack = 340;
  this.Defense = 15;
  this.speed = 50;
  this.cursedEnergy = 1350;
}
function panda(Health, Attack, Defense, Speed, cursedEnergy) {
  this.Health = 350;
  this.Attack = 45;
  this.Defense = 40;
  this.Speed = 35;
  this.cursedEnergy = 800;
}
function Nanami(Health, Attack, Defense, Speed, cursedEnergy) {
  this.Health = 250;
  this.Attack = 50;
  this.Defense = 25;
  this.Speed = 45;
  this.cursedEnergy = 1000;
}

function changeCharacter(character) {
  
  switch(character)
  {
      case "Mai":
        document.GetElementById("img").src = "assets/placeholdermai.png";
        document.GetElementById("name").innerHTML = "Mai Zen'in";
        break;
        
      case "Yuji":
        document.GetElementById("img").src = "assets/yuji.jpg";
        document.GetElementById("name").innerHTML = "Yuji Itadori";
        break;
      
      case "Panda":
        document.GetElementById("img").src = "assets/placeholderpanda.png";
        document.GetElementById("name").innerHTML = "Panda";
        break;
      
      case "Nanami":
        document.GetElementById("img").src = "assets/placeholdernanami.png";
        document.GetElementById("name").innerHTML = "Nanami";
        break;
  }  
  
}
