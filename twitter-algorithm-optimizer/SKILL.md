---
name: twitter-algorithm-optimizer
description: Analyze and optimize tweets for maximum reach using Twitter's open-source algorithm insights. Rewrite and edit user tweets to improve engagement and visibility based on how the recommendation system ranks content.
license: AGPL-3.0 (referencing Twitter's algorithm source)
---

# Twitter Algorithm Optimizer

## When to Use This Skill

- Optimize tweet drafts for maximum reach and engagement
- Understand why a tweet might not perform well algorithmically
- Rewrite tweets to align with Twitter's ranking mechanisms
- Improve content strategy based on the actual ranking algorithms
- Debug underperforming content and increase visibility

## What This Skill Does

1. Analyzes tweets against Twitter's core recommendation algorithms
2. Identifies optimization opportunities based on engagement signals
3. Rewrites and edits tweets to improve algorithmic ranking
4. Explains the "why" behind recommendations using algorithm insights
5. Applies Real-graph, SimClusters, and TwHIN principles to content strategy

## How It Works: Twitter's Algorithm Architecture

Twitter's recommendation system ranks tweets using several interconnected models:

- **Real-graph** — predicts whether a specific follower will engage with your content. Key signal: will they like, reply, or retweet this?
- **SimClusters** — detects communities of users with shared interests. Tweets that resonate deeply with a tight community outperform ones aimed at everyone.
- **TwHIN** — maps users and topics via knowledge-graph embeddings. Content clearly matching your established topic/identity ranks higher; unexplained topic jumps confuse it.
- **Tweepcred** — a reputation/authority score built from your engagement history. Higher credibility earns wider distribution.

**Engagement signals tracked** (Unified User Actions):
- Explicit, high-weight: likes, replies, retweets, quote tweets
- Implicit: profile visits, link clicks, time spent, saves/bookmarks
- Negative (penalized heavily): blocks/reports, mutes/unfollows, fast scroll-past

**Feed pipeline**: candidate retrieval (search index, following-graph, trending/viral sources) → ranking by predicted engagement → filtering (blocks/preferences) → delivery.

## Optimization Strategies

### 1. Maximize Real-graph (follower engagement)
Make content your followers will specifically engage with: reference topics they care about, ask direct questions (they drive replies more than statements do), tag related creators, post when your audience is active.
- ❌ "I think climate policy is important" → ✅ "Hot take: Current climate policy ignores nuclear energy. Thoughts?"

### 2. Leverage SimClusters (community resonance)
Pick one clear topic per tweet, use the community's own language/terminology, and be genuinely useful to that niche rather than broad.
- ❌ "I use many programming languages" → ✅ "Rust's ownership system is the most underrated feature. Here's why..."

### 3. Improve TwHIN mapping (content–identity fit)
Lead with domain knowledge, stay consistent with your established topics (or clearly signal a pivot), and reference past posts to build topical authority.
- ❌ "I like lots of things" → ✅ "My 3rd consecutive framework review as a full-stack engineer"

### 4. Boost Tweepcred (authority/credibility)
Reply to and quote high-credibility accounts with real value, avoid engagement bait (it doesn't build lasting credibility), and post consistently rather than chasing sporadic virality.
- ❌ "RETWEET IF..." → ✅ "Thoughtful critique of the approach in [linked tweet]"

### 5. Maximize engagement signals
Match the tweet's structure to the signal you want:
- **Likes**: novel insight, validation, or a strong opinion with evidence
- **Replies**: a direct question, a debate, or an incomplete thought inviting completion
- **Retweets**: useful, shareable, or representational content ("this speaks for me")
- **Bookmarks**: tutorials, data/stats, or reference material for later
- ❌ "Check out this tool" → ✅ "This tool saved me 5 hours this week. Here's how to set it up..."

### 6. Prevent negative signals
Avoid inflammatory or misleading content, harassment, off-brand pivots, and reply-guy behavior (too many low-value replies) — all of these get penalized and suppress future reach.

## How to Optimize a Tweet

1. **Identify the core message** — the single most important point, who should care, and what action/engagement you want.
2. **Map it to the algorithm** — which Real-graph segment, SimCluster community, and TwHIN identity does it fit? Does it help or hurt Tweepcred?
3. **Optimize for signals** — does it trigger replies (question/debate), retweets (useful/shareable), or likes (novel/validating)?
4. **Check against negatives** — any block/report risk, identity confusion, engagement bait, or inflammatory language?

## Example Optimizations

**Developer tweet**
- Original: "I fixed a bug today" — generic, no clear audience, no engagement trigger.
- Optimized: "Spent 2 hours debugging, turned out I was missing one semicolon. The best part? The linter didn't catch it. What's your most embarrassing bug? Drop it in replies 👇"
- Why it works: niche (developer) SimCluster resonance, a direct question drives Real-graph replies, and the vulnerability builds Tweepcred.

**Product launch tweet**
- Original: "We launched a new feature today. Check it out." — passive, no specific benefit, reads as self-promotion.
- Optimized: "Spent 6 months on the one feature our users asked for most: export to PDF. 10x improvement in report generation time. Already live. What export format do you want next?"
- Why it works: specific benefit ("10x improvement") triggers bookmarks, the closing question drives replies, and "6 months" signals authority.

## Best Practices

1. Quality over virality — consistent engagement from your community beats occasional viral moments
2. Deep resonance with a small engaged audience beats shallow reach to a large one
3. The algorithm rewards genuine engagement, not manipulation — avoid engagement pods/bots
4. Engage early (first hour) and reply to replies quickly; threads often outperform single tweets
5. Track what your specific audience engages with and iterate

## Common Pitfalls

- Generic, vague statements the algorithm can't route to any community
- Pure engagement bait ("Like if you agree") — hurts credibility long-term
- Unclear audience, off-brand topic pivots, or over-posting
- Toxicity (blocks/reports heavily penalize future reach)
- Passive tweets with no call to action

## When to Use This Skill vs. Plain Claude

Use this skill for: maximizing reach on a drafted tweet, diagnosing underperformance, or building audience in a specific niche.

Use Claude without this skill for: general writing/grammar fixes, tone adjustments unrelated to the algorithm, or non-Twitter content (LinkedIn, blogs, etc.).
