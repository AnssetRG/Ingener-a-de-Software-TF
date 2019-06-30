# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define A = Character("Aquiles", color = "ffffff") 
define L = Character("Lucina", color = "327cff")
define C = Character("Cordelia", color = "b8b832")
define T = Character("Titania", color = "ff3232")
define M = Character("Minerva", color = "ffff00")

# Declare any custom variable or flags
$ Rehenes = 0

# The game starts here.
label start:
    scene bg empire
    with Dissolve(0.5)
    
    "El suelo árido sobre el cual fue construido nuestro campamento está 
     ansioso por que empieze nuestro enfrentamiento."
    
    "La escaramuza a la aldea Portrian lleva 1 día de retraso por falta de 
     reconocimiento de los enemigos y, me atrevo a decir, la incopentencia 
     de mis exploradores."
    
    "Siento que estoy perdiendo la paciencia por seguir avanzando, pero 
     rodear la aldea nos llevaría varios días debido a su tan dañado terreno."
    
    "La infantería no tendría tantos problemas, pero el suelo 
     precipitado realentizaría drásticamente a nuestros caballos, carretas y 
     maquinaria que es vital para el asedio en la batalla de Marte."
    
    "Ya van pasando dos días desde que mandamos un embajador a hablar con la aldea 
     y que nos dejen pasar para estar todos en paz, pero solo nos han devuelto la 
     cabeza del primer mensajero."
    
    "De pronto, entró a mi tienda mi primera teniente y fiel compañera, Titania, 
     innterrumpiendo mis pensamientos con esta noticia."
    
    show titania calm at center
    T "Aquiles, los exploradores han avistado a nuestro último mensajero 
       en el camino de regreso."
    
    A "Gracias por avisarme, manda un par de guardias para que lo escolten hacia mi
       campamento lo antes posible. No queremos otra atrocidad como la última vez."
    
    T "Como ordene, general."
    hide titania calm
    scene bg black
    with Dissolve(0.5)
    
    "Por la expresión en su rostro, entiendo que quiere evitar la pelea contra esta 
     aldea. Al fin y al cabo, Portrian es una ciudad de bajos recursos, quedarían en
     desventaja contra un pelotón bien formado."
    
    "Pero por qué razón enviarnos el gesto amenzante de una cabeza decapitada? 
     Tengo entendido que allí yacen guerreras valientes e inquebrantables capaces de
     proteger su amado y tranqulo pueblo hasta la muerte."
    
    show lucina ready at center
    with Dissolve(0.5)
    
    "Había oído rumores acerca de eso siendo su mejor guerrera Lucina, una increible
     luchadora con alma incansable y voluntad de hierro, a quien conocí una vez cuando 
     visitó la capital de Roma, aquella vez no se me hubiera ocurrido que fuese 
     ella la gran guerrera de Portrian."
    
    "Ella había ido para solicitar apoyo contra unos invasores, pero el emperador 
     menospreciando sus habilidaes y su potencial le nego su petición, a pesar
     de haberme ofrecido y a mi batallón en su ayuda."
    
    "Se retiró con ira de la audiencia mirándome con un profundo rencor como si 
     yo hubiese sido la razón por la que el emperador negara su peticion. 
     Para luego decirme:"
    
    L "Solías ser alguien de inspiración para nuestra gente. Un modelo a 
       seguir tanto como soldado como persona. Pero me enferma ver como te quedas 
       ahí parado sin brindar ayuda sólo porque así lo decide tu emperador."
    
    L "Ahógense en su gloria, romanos."
    
    hide lucina ready
    scene bg empire
    with Dissolve(0.5)
    
    "Soldado romano" "General, el mensajero está solicitando su presencia."
    A "Que no se le haga esperar, hágalo pasar."
    
    # "Con firmeza salgo de la tienda y escucho al mensajero."
    
    # scene bg outside
    # with Dissolve(0.5)
    
    "Mensajero" "Aquiles, héroe de Troya y campeón del emperador. Le traigo noticias
                 urgentes de Portrian, lamentablemente no por palabra directa del 
                 monarca del pueblo ya que no pude ingresar al pueblo."
    
    A "Hable mensajero, dígame lo que ocurrió ahí fuera."
    
    "Mensajero" "La única entrada al pueblo está reforzada y vigilada a todo momento. 
                 La primera respuesta al acercarse es un ataque de flechas como aviso."
    
    "Mensajero" "De la misma manera, mientras me retiraba después de multiples intentos
                 esuché gritos de su parte diciendo: \"Fuera escoria romana!\"."
    
    show titania calm at left
    T "Me duele creerlo."
    
    "Titania sabe lo que eso significa, su rostro muestra incomodidad con respecto a 
     cómo se desenvolverán las cosas de ahora en adelante con la gente de ese pueblo."
    
    A "Gracias por tu servicio noble mensajero, puedes retirarte a descansar."
    
    "Necesito hablar con mi primera teniente al respecto, necesito de sus consejos y
     ella necesita hablar con alguien ahora mismo acerca de lo que sucederá."
    
    show titania calm at center
    
    A "Titania, quiero hablar contigo un momento a solas."
    T "Sí, mi señor."
    
    A "Esto es importante y necesito de tu sinceridad. ¿Cómo crees que deberíamos 
       proseguir con la situación en Portrian?"
    
    T "Aquiles, sabe que no me agrada cuando se trata de quitarle la vida a las
       personas. Propondría que las matanzas se mantengan al mínimo, pero aquí es 
       usted quien manda y seguiremos sus ordenes."
    
    A "Entiendo... sin embargo no puedo prometerte que nadie morirá. Ahora debemos
       alistarnos para partir hacia allá."
    
    scene bg black
    with Dissolve(0.5)
    
    "Hemos recorrido un largo camino hasta aquí, debemos de estar por llegar a las
     afueras de Portrian en cualquier momento. Sin embargo, aun no tengo en claro 
     qué es lo que haremos con los habitantes del pueblo."
    
    "Han pasado horas desde que salimos de Roma y veo que Titania aun continua con ese
     gesto en su rostro, probablemente sigue pensando en lo que sucederá."
    
    scene bg village
    with Dissolve(0.5)
    
    "Finalmente, hemos llegado a las afueras del pueblo y a buen tiempo también, es de
     noche con luna nueva, eso debería ayudarnos a entrar desapercibidos en cuanto hagan
     el cambio de guardia."
    
    "El plan resultó cómo lo esperaba, logramos entrar sin que lo notaran, es hora de 
     abrirse paso hasta el monarca."
    
    show titania calm at left 
    with Dissolve(0.5) # Deslizar desde el borde
    
    A "Titania, tú y tus tropas encárguense de sacar a todas las personas de sus hogares,
       agrúpalos y manténlos contenidos. Si se encuentran con un grupo de soldados 
       acaben con ellos sigilosamente, no queremos que se enteren que estamos aquí."
    
    T "Entendido, Señor. Me pregunto, qué planeas hacer con todas esas personas?"
    
    A "Aún no lo tengo en claro...  Sé que deseas evitar muertes innecesarias, 
       pero puede que no nos dejen otra opción."
    
    T "Entiendo que no sea una decisión sencilla, mi Señor, espero tome la decisión 
       correcta. Por otro lado, qué hará Ud. mientras tanto?"
    
    A "Debo dirigirme hacia el monarca de Portrian, después de las atrozidades que le
       hizo a los mensajeros que envíamos veo difícil que podamos perdonarle la vida."
    
    show titania ready at left
    
    A "Muy bien en movimiento! Debemos apurarnos antes que se haga de día, no queremos
       más pelotones de soldados rondando."
    
    hide titania ready
    # scene bg towndoor
    with Dissolve(0.5) # Deslizar al borde de pantalla
    
    A "Hemos llegado ya a la cámara del monarca. Sin embargo, no ha sido difícil haber
       llegado hasta aquí, no nos hemos tenido que encargar de tantos guardias."
    
    A "Tengo un mal presentimiento de esto... estén preparados mis soldados. Adelante!"
    
    # scene bg townhall 
    # with Dissolve(0.5)
    
    "Monarca" "Le estaba esperando, Aquiles... Sabía que vendría después que mis soldados
               dejaran escapar a ese mensajero tuyo. Sin embargo, no esperaba un grupo
               tan pequeño de soldados para invadir un pueblo como este."
    
    show lucina calm at right
    with Dissolve(0.5) # Deslizar desde borde de pantalla
    
    L "Le dije que vendrían, señor Zimbael, tuvimos que habernos hecho cargo de esa
       escoria de mensajero romano. Permitame eliminar a todos los romanos presentes."
    
    A "Por fin combate decente en este pequeño pueblo olvidado, ha sido demasiado fácil
       hasta ahora."
    
    show lucina ready at right
    
    L "Qué dijiste!? No esperes ver la luz del día Aquiles!"
    
    "Zimbael" "Lucina, cálmate. Sé que no somos tu objetivo principal, Aquiles, sé que
               planeas atacar Marte después de Portrian, sólo somos un obstáculo en el
               camino para ti."
    
    "Zimbael" "Bueno... que te parece si acabamos esto aquí y ahora, Aquiles."
    
    "Zimbael" "Soldados! Acaben con la escoria romana..."
    
    A "Por fin terminó la charla? me estaba poniendo impaciente."
    
    scene bg black
    with Dissolve(0.5)
    
    "Después de todo, logramos salir victoriosos a pesar de haber perdido un número
     considerable de tropas. Tendremos que reabastecernos y traer refuerzos antes de
     continuar con la invasión a Marte."
    
    "Por otro lado, no puedo creer que Lucina lograra escapar, conociendo su naturaleza
     vengativa supongo que esta no será la última vez que la veremos."
    
    "Pero no es momento de estar pensando en qué podría pasar con Lucinac
     Ahora debo encontrarme con Titania para determinar qué haremos con los pobladores
     de Portrian."
    
    scene bg village
    with Dissolve(0.5)
    
    menu:
        "Matar a todos":
            jump MatarGente
            
        "Tomarlos como rehenes":
            jump RehenesGente
            
        "Dejarlos ir":
            jump IgnorarGente

    return

label MatarGente:
    A "Acaben con todos, que no quede ni uno vivo, no queremos que uno de ellos
       vaya a Marte a reportar la invasión al pueblo de Portrian."
            
    A "Si uno de ellos logra avisarles, podríamos perder el elemento sorpresa
       el cual puede ser clave para el asedio a Marte."
    
    scene bg black
    with Dissolve(0.5)

    "Lo lamento, Titania… tendré que romper mi promesa, no puedo tomar chance al
     error, necesitamos esta ventaja contra el imperio enemigo."
            
    "Ha sido una tarea desagradable de realizar, pero ya está hecho, debemos
     continuar."
            
    "Nos infiltraremos por el alcantarillado del imperio enemigo, eso debería 
     llevarnos hasta la cámara real del palacio."
    
    $ Rehenes = 0
    jump Act2
    return
    
label RehenesGente:
    A "No los maten, los utilizaremos como prisioneros para abrirnos paso por la
       puerta principal de Marte."
  
    show titania calm at left
    with Dissolve(0.5) # Deslizar desde borde de pantalla
  
    T "Aquiles, debe de haber una mejor opción para ellos."
  
    A "Lo lamento Titania, pero pueden ser un elemento clave en la invasión. Prometo
       liberarlos después de esto, pero los necesitamos ahora mismo para entrar a 
       Marte por la puerta principal."
  
    T "Espero que tengas en claro lo que estás haciendo Aquiles."
  
    $ Rehenes = 1
    jump FrontDoor
    return
    
label IgnorarGente:
    A "Déjenlos ir, no nos son de utilidad ahora mismo. Además, ya han visto
       sufrimiento tras la invasión a su pequeño pueblo."
  
    show titania calm at left
    with Dissolve(0.5) # Deslizar desde borde de pantalla
  
    T "Estoy de acuerdo, no es necesaria más matanza en Portrian, espero que puedan
       retomar sus actividades cotidianas. Gracias por no hacerles daño, señor."
  
    A "Ahora debemos concentrarnos más en elegir por donde continuaremos el ataque a
       Marte."
  
    T "Hemos divisado que existen 2 posibles entradas, podríamos trepar la muralla del
       palacio o abrirnos paso a través de la puerta principal de este."
  
    A "La primera es sigilosa, pordíamos escabullirnos hasta la cámara real del
       palacio sin levantar sospechas."
  
    A "La segunda es una entrada más directa teniendo que pelear contra cada soldado
       que se cruce en nuestro camino."
    
    hide titania calm
    with Dissolve(0.5)
    
    $ Rehenes = 2
    menu:
        "Puerta principal":
            jump FrontDoor
            
        "Trepar Muralla":
            jump ClimbWall
    return
    
label FrontDoor:
    scene bg ruins
    with Dissolve(0.5)
    
    A "Entraremos por la puerta principal, alisten sus armas, vamos a tener que
       abrirnos paso a través de los múltiples pelotones de soldados."
    
    if Rehenes == 1:
        
        show titania calm at left
        with Dissolve(0.5)
        
        A "Tenemos rehenes! Dejennos pasar hasta la cámara real del palacio y 
           ellos no tendrán que morir."
        
        T "Hagan lo que dice, estos son los últimos ciudadanos de Portrian"
        
        "Soldado" "Está bien, pueden ingresar a Marte..."
        
        A "Veo que son sensatos. Bien, no intenten nada o eliminaremos a los rehenes.
           Avancemos mi gente."
        
        "Soldado" "Muy bien señores, ya los tenemos dentro del palacio."
        
        show titania ready at left
        
        "Soldado" "Eliminen a las ratas de Portrian..."
        
        T "Una Emboscada!?"
        
        A "Maldición! No les importó en lo más mínimo que los tuvieramos de rehenes,
           los han aniquilado como cerdos en matadero."
        
        T "Esta gente de Marte va a pagar por las acciones cometidas en contra de 
           los inocentes, sus vidas no necesitaban acabar así."
        
    A "Adelante, no dejen que ninguno de estos soldados de Marte salgan con vida.
       No tenemos otra opción más que eliminarlos para pasar."
    
    A "Si seguimos así llegaremos a la camara real con menos de la mitad del
       pelotón, pero al menos ya logramos salir victoriosos de este combate."
    
    A "Espero no se nos acerquen más unidades hasta que logremos llegar. No debe de
       faltar mucho para llegar."
    
    hide titania ready
    jump Act2
    return
    
label ClimbWall:
    scene bg ruins
    with Dissolve(0.5)
    
    A "Traigan las escaleras, treparemos el muro y trataremos de llegar a la cámara
       real desapercibidos, si encontramos algunos guardias los eliminamos en
       sigilo."
    
    "Romano" "Señor, la escalera está por llegar."
    
    A "Perfecto, vamos a trepar, adelante!"
    
    A "mmhh veo que hay algunos guardias en la entrada a la cámara real, tendremos
       que disponer de ellos si queremos entrar."
    
    "Soldado" "Alto ahi, quién anda ahí? No pasará nadie sobre mi cadav-"
    
    A "Silencio bastardo. Seremos nosotros los que pasaremos sobre ti."
    
    jump Act2
    return
    
label Act2:
    scene bg ruins
    show titania calm at right
    with Dissolve(0.5)
    
    "Por fin, después de una gran travesía, hemos llegado a la cámara real
     del palacio. Me preocupa que hayamos llegado hasta aquí por nada."
     
    A "Titania, reporte de bajas."
                                   
    T "Aun tenemos por lo menos la mitad de nuestra gente Aquiles, pero no podríamos
       soportar otro gran ataque enemigo."
    
    "Algo anda mal... dónde están las personas, debería haber gente al rededor y dentro
     del palacio, pero no nos hemos encontrado con ningún civil"
    
    L "Ríndete escoria romana, te tenemos rodeado!"
    
    show titania ready at right
    T "Una emboscada de Lucina!"
    
    A "Titania quédate atrás, trataré de arreglar esto directamente con ella."
    
    show lucina ready at left
    with Dissolve(0.5)

    if Rehenes == 0:
        A "Qué te parece un duelo maldita inútil?"
        
        L "Cómo has osado llamarme...!?"
        
        A "Ya me oíste! tú y yo un duelo uno contra uno! Vencerá únicamente el que
           quede en pie... que seré yo obviamente."
        
        "Lo que ella no sabe es que yo, el gran Aquiles, he sido bendecido por los
         dioses con una protección divina."
        
        L "Pues bien, en cuanto acabe contigo Roma quedará debilitada y nosotros
           retaliaremos."
        
        show titania calm at right
        T "Tenga cuidado, señor Aquiles."
        jump QuitarProt
        
    if Rehenes == 1:
        hide titania calm
        with Dissolve(0.5)
        
        A "Te reto a un duelo a muerte Lucina, no hay necesidad de esparcir más sangre.
           Arreglemos las cosas sólo entre nosotros."
        
        L "Me parece bien, en cuanto acabe contigo Roma quedará debilitada y nosotros 
           retaliaremos, tendremos nuestra venganza sobre Roma."
        
        jump Enfrentamiento
        
    if Rehenes == 2:
        hide titania calm
        with Dissolve(0.5)
        
        A "Arreglemos esto con un duelo uno contra uno, tú y yo, Lucina. No quiero que
           se desperdicien más vidas."
        
        L "No, después de haber visto que dejaste escapar a la gente de Portrian, veo
           que no eres tan arrogante como lo pensaba, quizás podríamos llegar a un acuerdo"
        
        "Un acuerdo? mmhh... podría ser una trampa."
        
        menu:
            "Insistir en duelo":
                A "No, esto debe acabar con sólo uno de nosotros en pie. No puedo permitir
                   que sigas andando por ahí."
                
                jump Enfrentamiento
            
            "Aceptar dialogar":
                A "Muy bien, habla... qué tienes que decir?"
                
                jump Dialogo
    return

label QuitarProt:
    scene bg black
    hide titania calm
    with Dissolve(0.5)
    
    "Creía poder recibir cualquier cosa sin sufrir ningún daño... pero qúe es esto!?"
    
    "Su espada ha atravesado mi pecho. Dónde quedó mi protección divina? Es este en 
     realidad el final? Será que estoy muriendo realmente?"
    
    #scene bg white
    hide lucina ready
    show minerva calm at left
    show cordelia calm at right
    with Dissolve(0.5)
    
    M "Aquiles, mi nombre es minerva, diosa de la sabiduría y la estrategia militar.
       Tu dichosa protección divina se te fue removida por las fechorías que has
       cometido."
    
    M "Has logrado exterminar un pueblo entero, habían personas inocentes que no
       merecían tal castigo."
    
    A "Creía que mi protección me llevarpia a la grandeza y terminé ciego por su 
       gran poder. Seguir adelante sin pensar en las consecuencias de mis acciones."
    
    C "Y ahí es donde reside tu error, Aquiles. Tener un gran poder no te exonera de
       consecuencias. Ahora te han llegado las consecuencias."
    
    M "La hora te ha llegado por fin. Reúnete con tus ancestros."
    
    C "Descansa ya, nuestro valiente guerrero. Nos habíamos equivocado contigo"
    
    scene bg black
    hide minerva calm
    hide cordelia calm
    with Dissolve(0.5)
    
    "Lo lamento, Titania. Pero no nos volveremos a ver de nuevo."
    
    jump BadEnding
    return
    
label Enfrentamiento:
    "Lucina tiene grandes habilidades para el ataque debo de estar preparado para 
     cualquier ataque que vaya a realizar. Por otro lado, tengo mi protección divina
     para que me proteja, podría comenzar el ataque yo y no dejarle moverse."
    
    menu:
        "Pelear ofensivo":
            "Debo atacarle, no le daré chance a que me lo devuelva"
            
            scene bg black
            hide lucina ready
            with Dissolve(0.5)
            
            L "Eres un estúpido Aquiles, estuve analizando tu forma de pelear y cómo
               siempre defiendes tu talón derecho"
            
            A "Diablos! Cómo lo descubrió?"
            
            L "Esta victoria es mía ahora al haberte lanzado a mí has descubierto tu talón."
            
            "Es muy tarde para tirarse para atrás, estoy perdido. Me descuidé y ahora lo 
             pagaré."
            jump BadEnding
            
        "Pelear defensivo":
            "Gracias a mi bendición sólo tengo que quedarme atrás defendiéndome de sus 
             ataques hasta que se exponga demasiado en una ocasión y la victoria será mía"
            
            A "Acércate, o es que tienes miedo?"
            
            L "Última vez que escucho algo de ti escoria romana."
            
            "Lo logré, la provoqué lo suficiente para que me atacara. Está perdida."
            
            "Victoria"
            
            A "Has peleado bien Lucina, ahora descansa y reúnete con tus ancestros, no hay
               necesidad de más sangre. Se acabó"
            
            jump NeutralEnding
    return
    
label Dialogo:
    L "Me sorprendió cuando me enteré que habías dejado huir a nuestra gente. Al 
       comienzo creí que todo era una mentira. Sin embargo, parece ser que era verdad
       después de todo."
    
    A "No quise seguir tomando vidas en Portrian, sólo las que se nos fueran necesarias
       para avanzar con nuestro ataque a Marte. Por otro lado, eran únicamente civiles,
       no tenían como defenderse y estaban aterrados, no tenían porqué morir."
    
    L "Veo que no eres tan desalmado y necio como te pintaban algunas personas en
       Portrian, simplemente te concentras demasiado en alcanzar tus objetivos que 
       aparentas serlo."
    
    A "Si me detuviese a pensar cada vida que tengo que tomar para seguir adelante no 
       sería capaz de proteger Roma. Las cosas que hago son únicamente para fortalecer
       y ayudar a mi gente. Ellos son mi prioridad."
    
    L "Quisiera que formemos una alianza que Portrian sea parte del imperio romano, 
       podríamos brindarte fenomenales guerreros para que puedas cumplir tus objetivos
       mientras que nos des los suficientes recursos para lograrlo."
    
    A "No suena a una mala idea, pero ya me había hecho cargo del monarca. Quién se 
       haría cargo de Portrian?"
    
    L "Yo lo haría, me convertiría en la nueva monarca de Portrian y serían mi gente.
       Después de todo, yo ya era considerada la mano derecha de Zimbael así que no creo
       que a nadie le sorprenda que sea yo la siguiente líder del pueblo."
    
    A "Entonces queda hecho, de ahora en adelante Portrian no sufrirá más. Serán parte
       de Roma y lograremos grandezas con uds a nuestro lado."
    
    L "Me alegra que hayamos podido llegar a un acuerdo, Aquiles."
    
    jump GoodEnding
    return

label BadEnding:
    scene bg ruins
    show titania calm at right
    with Dissolve(0.5)
    
    "Romano" "Teniente, me temo imformarle que el capitan ha muerto."
    
    T "Imposible... Dónde se encuentra?"
    
    show lucina calm at left
    with Dissolve(0.5)
    
    L "Llévaleto, regresen a su mugrienta Roma... y estén preparados porque esto no
       se acabará aquí."
    
    T "Qué le has hecho? Cómo es esto posible, nunca antes había sido derrotado."
    
    L "No los eliminaremos porque no importa que hagan, sin él no podrán aguantar.
       Lárgate de aquí, informen a toda Roma que aquí cayó su campeón y que sepan
       que no les quedará mucho tiempo restante."
    
    return

label NeutralEnding:
    scene bg ruins
    show titania calm at right
    with Dissolve(0.5)
    
    A "Se acabó, hemos ganado. No será necesaria más matanza, Marte es nuestra. La
       conquista ha resultado tediosa, han muerto demasiadas personas para llegar
       aquí, tanto aliados, enemigos y civiles. No se repetirá."
    
    A "Pero esta noche, cantamos victoria!"
    
    A "Teniente, deme un reporte de la situación y mande un mensajero de vuelta a
       Roma avisando nuestra victoria."
    
    T "Entendido, señor. Resultamos con la mitad de nuestro pelotón. Las últimas
       unidades de Portrian se retiraron tras la caída de Lucina."
    
    if Rehenes == 1:
        T "Desafortunadamente los rehenes que habíamos tomado fueron asesinados.
           Fue un movimiento inesperado de parte del enemigo."
        
        T "Hubiera deseado que pudieramos dejarlos ir."
        
    if Rehenes == 2:
        T "Y me alegra que hayamos dejado ir a las personas de Portrian, merecían
           continuar con sus vidas tranquilas."
    return

label GoodEnding:
    scene bg landscape
    show lucina calm at right
    with Dissolve(0.5)
    
    "Ha pasado un año desde la invasión a Marte. La unión entre Portrian y Roma fue 
     una gran idea, ahora somos más fúerte que nunca."
    
    A "Por fin, se acabaron los conflictos entre Portrian y Roma y hemos eliminado
       el imperio tirano de Marte."
    
    L "Sin duda el haberme unido a ti y tus fuerzas resultó mejor de lo que tenía
       en mente. Y veo que hemos progresado bastante en la alianza formada esa vez."
    
    A "Sí... Está dando fruto a pesar que al comienzo eramos enemigos."
    
    L "Hablando de dar frutos..."
    
    A "Lucina? Qué tienes en mente...?"
    
    L "Quería saber... si... Quisieras casarte conmigo?"
    
    A "Lucina!"
    
    L "Lo siento, no debí decirlo de esa manera, mucho menos en este momento. Olvida
       que dije eso, por favor."
    
    A "No te preocupes, iba a decir que sí, de hecho..."
    
    A "Le pediré a mi gente que preparen todo lo necesario para que se dé."
    
    "Y así es como terminaron las cosas después de todo, eh? Creo que no pudo haber 
     terminado de una mejor manera."
    return





