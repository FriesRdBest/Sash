## Sinch product surface

- **Verification API** — OTP via SMS/voice. [Docs](https://developers.sinch.com/docs/verification)
- **Messaging API** — SMS, MMS, RCS. [Docs](https://developers.sinch.com/docs/messaging)
- **Voice API** — inbound/outbound calls, IVR. [Docs](https://developers.sinch.com/docs/voice)

**Reference**: [Sinch Developers](https://developers.sinch.com/)
## Relevant Sinch products

### Verification API

Purpose: Verify phone numbers during user registration.

Key capabilities:
- SMS verification codes
- Voice call verification
- Flash call verification
- Data verification (app-to-app)
- Status callbacks for verification events

Documentation: https://developers.sinch.com/docs/verification

### Messaging API

Purpose: Send SMS, MMS, WhatsApp, and other channel messages.

Key capabilities:
- Send and receive messages
- Delivery reports
- Inbound webhooks
- Sender ID configuration
- Country-specific routing and compliance

Documentation: https://developers.sinch.com/

### Conversation API

Purpose: Unified interface for multiple messaging channels.

Key capabilities:
- Channel routing (SMS, WhatsApp, Messenger, Viber, RCS)
- Intelligent fallback
- Unified delivery events
- Conversation state management

Documentation: https://sinch.com/messaging/conversation-api

### Voice API

Purpose: Make and receive voice calls.

Key capabilities:
- Outbound calls for verification
- Call flows and IVR
- Recording and transcription
- Webhooks for call events

Documentation: https://developers.sinch.com/docs/voice

## Callback and event model

Sinch provides delivery status through:

- **Delivery reports**: Message delivery status (sent, delivered, failed)
- **Inbound webhooks**: User replies and opt-out events
- **Verification status**: Verification success or failure events

All events include:
- Message or verification ID
- Timestamp
- Status code
- Recipient number
- Optional error details

## Authentication

Sinch APIs use:
- API keys (for server-to-server)
- OAuth 2.0 (for user-facing applications)
- HMAC signature validation for webhooks

## Rate limits and quotas

- Verification API: Varies by country and account tier
- Messaging API: Depends on channel and destination
- Voice API: Concurrent call limits apply

Consult Sinch documentation for current limits.

## Regional considerations

- Phone number formatting varies by country
- Sender ID restrictions apply in some markets
- WhatsApp template approval required for business-initiated messages
- Data residency requirements may apply

## Integration patterns

Common patterns for verification workflows:

1. **Direct Verification API**: Use Sinch Verification for simple phone number verification
2. **Custom workflow**: Use Messaging API + Conversation API for multi-channel fallback
3. **Voice fallback**: Use Voice API if SMS delivery fails

## References

- Sinch Developer Documentation: https://developers.sinch.com
- Conversation API webhooks: https://sinch.com/messaging/conversation-api/intelligent-routing-webhooks
- Verification API: https://developers.sinch.com/docs/verification/introduction
