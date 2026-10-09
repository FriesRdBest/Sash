# Provider capability matrix

This document compares SMS, WhatsApp, and email channel characteristics for the Aurora Marketplace verification workflow.

## Channel comparison

| Capability | SMS | WhatsApp | Email |
|---|---|---|---|
| **Delivery speed** | Seconds | Seconds | Seconds to minutes |
| **Reliability** | High | High | Medium |
| **Cost per message** | Medium | Low | Very low |
| **User friction** | Low | Medium | Low |
| **Template approval** | Not required | Required for business-initiated | Not required |
| **Two-way communication** | Yes | Yes | Yes |
| **Delivery reports** | Yes | Yes | Yes |
| **Fallback suitability** | Primary | Fallback | Fallback |
| **Regional restrictions** | Sender ID rules | Business verification | SPF/DKIM setup |
| **Opt-in requirements** | Varies by country | Required | Required (CAN-SPAM, GDPR) |

## SMS characteristics

**Strengths:**
- Universal reach (works on all mobile phones)
- High open rates
- Fast delivery
- No app required

**Weaknesses:**
- Higher cost than alternatives
- Character limits (160 chars per segment)
- Sender ID restrictions in some countries
- Potential carrier filtering

**Best for:** Primary verification channel

## WhatsApp characteristics

**Strengths:**
- Rich media support
- Low cost
- High engagement
- End-to-end encryption

**Weaknesses:**
- Requires WhatsApp app
- Business account verification
- Template approval for business-initiated messages
- 24-hour session window for user-initiated messages

**Best for:** Fallback when SMS fails or for users who prefer messaging apps

## Email characteristics

**Strengths:**
- Very low cost
- No character limits
- Rich formatting
- Universal

**Weaknesses:**
- Slower delivery
- Lower open rates for verification
- Spam folder risk
- Requires email client access

**Best for:** Fallback when mobile channels fail, or for users without mobile access

## Routing strategy

Recommended priority:

1. **SMS** (primary) — fastest, most universal for verification
2. **WhatsApp** (fallback 1) — if SMS fails or user prefers
3. **Email** (fallback 2) — if mobile channels fail

## Delivery event handling

All channels provide:

- Sent event
- Delivered event (with varying reliability)
- Failed event (with error codes)
- Inbound event (user replies)

Sash normalizes all channel events to a common schema.

## Compliance considerations

- **SMS:** TCPA (US), GDPR (EU), local sender ID registration
- **WhatsApp:** WhatsApp Business Policy, template approval
- **Email:** CAN-SPAM (US), GDPR (EU), CASL (Canada)

## References

- Sinch Messaging API: https://developers.sinch.com/docs/messaging
- WhatsApp Business API: https://developers.facebook.com/docs/whatsapp
- Sinch Conversation API routing: https://sinch.com/messaging/conversation-api/intelligent-routing-webhooks
