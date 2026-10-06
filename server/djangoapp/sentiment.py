"""Tiny lexicon-based sentiment analyzer for customer reviews."""

POSITIVE = {
    'fantastic', 'great', 'excellent', 'awesome', 'amazing', 'wonderful', 'love',
    'loved', 'best', 'good', 'friendly', 'helpful', 'fast', 'clean', 'happy',
    'perfect', 'pleased', 'satisfied', 'recommend', 'services', 'service',
}
NEGATIVE = {
    'terrible', 'awful', 'bad', 'worst', 'hate', 'hated', 'slow', 'rude',
    'dirty', 'poor', 'disappointed', 'horrible', 'never', 'waste', 'broken',
}


def analyze_sentiment(text):
    """Return {'label': positive|negative|neutral, 'score': float} for text."""
    words = {w.strip('.,!?"\'').lower() for w in (text or '').split()}
    pos = len(words & POSITIVE)
    neg = len(words & NEGATIVE)
    total = max(len(words), 1)
    if pos > neg:
        return {'label': 'positive', 'score': round(pos / total, 3)}
    if neg > pos:
        return {'label': 'negative', 'score': round(-neg / total, 3)}
    return {'label': 'neutral', 'score': 0.0}
