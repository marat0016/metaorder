package g_app.utils;

/***
 * Represents inclusive-exclusive range [start, end)
 * @param <E>
 */
public class Range<E extends Comparable<E>> {
    private E start;
    private E end;

    public Range(E start, E end) {
        this.start = start;
        this.end = end;
    }

    /**  Check tha value lies in inclusive-exclusive range [start, end) */
    public boolean isInRabge(E value) {
        return start.compareTo(value) <= 0 && end.compareTo(value) > 0;
    }
}
