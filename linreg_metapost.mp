beginfig(1)
	  pair A, B, C, D, E,F,G,H,I, K, L, EA, FA, GA, HA, IA;
    A=(-0.5cm,0cm); B=(6cm,0cm); C=(0cm,-0.5cm);D=(0cm,5cm);

		E=(1cm,1cm);F=(2cm,3cm);G=(3cm,2cm);H=(4cm,4cm);I=(5cm,2cm);
		EA=(1cm,1.8cm);FA=(2cm,2.1cm);GA=(3cm,2.4cm);HA=(4cm,2.7cm);IA=(5cm,3cm);		
		K=(0cm,1.5cm);L=(6cm,3.3cm);
    drawarrow A--B;
    drawarrow C--D;
    
    draw K--L withcolor blue;
    
    draw E--EA withcolor red;
    draw F--FA withcolor red;        
    draw G--GA withcolor red;    
    draw H--HA withcolor red;
    draw I--IA withcolor red;        
    
    draw E withpen pencircle scaled 2bp;
    draw F withpen pencircle scaled 2bp;
    draw G withpen pencircle scaled 2bp;
    draw H withpen pencircle scaled 2bp;
    draw I withpen pencircle scaled 2bp;
    
    draw EA withpen pencircle scaled 2bp withcolor green;
    draw FA withpen pencircle scaled 2bp withcolor green;
    draw GA withpen pencircle scaled 2bp withcolor green;
    draw HA withpen pencircle scaled 2bp withcolor green;
    draw IA withpen pencircle scaled 2bp withcolor green;
endfig;