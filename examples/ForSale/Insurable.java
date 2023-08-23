public interface Insurable extends Sellable, Transportable {
    /** Returns insured value in cents */
    public int insuredValue();
}