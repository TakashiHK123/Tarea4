//En este codigo no esta implementado la funcionalidad de una PID con motor, simulamos la comunicacion con la GUI dependiendo de la situacion
//void (*funcReset)()=0; 
void setup() {   
  Serial.begin(9600);
  delay(30);  

 
}
int posicion_cadena,posicion_motor,kp_pid,ki_pid,kd_pid,velocidad_motor,voltaje,corriente,velocidad_motor1,posicion_motorE;
String posicionMotor,kp,ki,kd,cadena,i2cbus,cadenaEnviar,velocidad_motorString,i2cString,posicion_String,voltaje_String,corriente_String,kp_String,ki_String,kd_String,estado;

void loop() {     //Recibimos por serial codigo ascii del python 
    //La GUI al enviar los datos de posicion, kp, ki, kd, lo cual es lo necesario, el PID se encargara de darle una velocidad, pero nosotros solo  estamos simulando el comportamiento asi que le damos un valor X a la velocidad
  if(Serial.available()){
    //Simulamos unos valores 
    i2cString="0xb1";
    cadena = Serial.readString(); 
    posicion_cadena = cadena.indexOf(',');           //separamos la cadena lo que viene entre coma , 
    posicionMotor= cadena.substring(0,posicion_cadena);    //se guarda lo que esta antes de la coma 
    kp = cadena.substring(posicion_cadena+1);    //se guarda lo que esta luego de la coma
    ki = cadena.substring(posicion_cadena+2); 
    kd = cadena.substring(posicion_cadena+3);
    //Pasamos a int los string respectivamente para usarse luego en el PID 
    if(posicion_motorE != posicionMotor.toInt()){          
      posicion_motorE = posicionMotor.toInt();
    }
    if(kp_pid != kp.toInt()){
      kp_pid = kp.toInt();
    }
    if(ki_pid != ki.toInt()){
      ki_pid = ki.toInt();
    }
    if(kd_pid != kd.toInt()){
      kd_pid = kd.toInt();
    }
    if(posicion_motorE==0 && kp_pid==0 && ki_pid==0 && kd_pid==0){
  
      //Aqui apagamos el motor 
      //Simulamos que el motor se apago
      cadenaEnviar="0,0,0,0,0x00"; 
      Serial.println(cadenaEnviar);
    }
      
      //funcReset();
    
      //Convertimos los valores a string para concatenar y enviar
      velocidad_motor=45;
      voltaje=12; 
      corriente=2;
      i2cString="0xb0";
      velocidad_motorString = (String) velocidad_motor;
      posicion_String = (String) posicion_motorE;
      voltaje_String = (String) voltaje;
      corriente_String = (String) corriente;
      kp_String = (String) kp_pid;
      ki_String = (String) ki_pid;
      kd_String = (String) kd_pid;
      cadenaEnviar=velocidad_motorString+","+posicion_String+","+"12"+","+corriente_String+","+i2cString;  
      Serial.println(cadenaEnviar);
      //funcReset();
    
    

    
  }else{
    //Simulamos que el arduino le envia siempre los siguientes datos a la GUI en modo automatico
    //Convertimos los valores a string para concatenar y enviar
      posicion_motor=14;
      velocidad_motor1=30;
      voltaje=11;
      corriente=1;
      i2cString="0xb2";
      velocidad_motorString = (String) velocidad_motor1;
      posicion_String = (String) posicion_motor;
      voltaje_String = (String) voltaje;
      corriente_String = (String) corriente;
      kp_String = (String) kp_pid;
      ki_String = (String) ki_pid;
      kd_String = (String) kd_pid;
    cadenaEnviar=velocidad_motorString+","+posicion_String+","+voltaje_String+","+corriente_String+","+i2cString; 
    Serial.println(cadenaEnviar);
  }
  
}
