//(c) A+ Computer Science
//www.apluscompsci.com
//Name -
//Date -

import static java.lang.System.*;
import java.awt.Color;

public class CardTestOne
{
	public static void main( String args[] )
	{
		Card one = new BlackJackCard();
		System.out.println(one);

		Card two = new BlackJackCard(1,"DIAMONDS");
		System.out.println(two);

		Card three = new BlackJackCard(4,"CLUBS");
		System.out.println(three);
		
		Card four = new BlackJackCard(12,"SPADES");
		System.out.println(four);
	
		Card five = new BlackJackCard(12,"HEARTS");
		System.out.println(five);	
		
		Card six = new BlackJackCard(9,"SPADES");
		System.out.println(six);				

		System.out.println(one.equals(two));
		System.out.println(one.equals(one));		
		System.out.println(four.equals(five));	
		System.out.println(three.equals(four));						
	}
}