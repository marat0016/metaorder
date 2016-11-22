package g_app;

import g_app.utils.Range;
import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class RangeTest {
	Range<Integer> testRange1 = new Range<Integer>(-1, 6);
	Range<Integer> invTestRange = new Range<Integer>(10, -3);

    @Test
    public void testSimpleRange() {
		Assert.assertTrue(testRange1.isInRabge(-1));
		Assert.assertTrue(testRange1.isInRabge(5));
		Assert.assertTrue(!testRange1.isInRabge(6));
    }

	@Test
	public void testInverseRange() {
		Assert.assertTrue(!invTestRange.isInRabge(10));
		Assert.assertTrue(!invTestRange.isInRabge(-3));
		Assert.assertTrue(!invTestRange.isInRabge(0));
	}
}