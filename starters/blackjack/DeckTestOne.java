//(c) A+ Computer Science
//www.apluscompsci.com
//Name -
//Date -

public class DeckTestOne
{
	public static void main( String args[] )
	{
		Deck deck = new Deck();	
		for( int i=0; i<Deck.NUMCARDS; i++ ) {
		  System.out.println(deck.nextCard());
		}
		
		System.out.println("\n\n");
		
		System.out.println("num cards left in the deck == " + deck.numCardsLeft());
		
		System.out.println("\n\nshuffling");
		deck.shuffle();
		System.out.println("num cards left in the deck == " + deck.numCardsLeft());
		
		
		System.out.println("\n\ntoString");
		System.out.println(deck);							
	}
}