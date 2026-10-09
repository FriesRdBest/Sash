# System context diagram

This document describes the system context for Sash.

## Context

Sash operates between Aurora Marketplace (the customer) and Sinch (the communications provider).

```
┌──────────────────────────────────────────────────────────────────┐
│                         Aurora Marketplace                       │
│  ┌────────────┐    ┌────────────┐    ┌────────────┐             │
│  │  Signup    │    │   User     │    │ Operations │             │
│  │  Form      │    │  Device    │    │  Dashboard │             │
│  └─────┬──────┘    └─────┬──────┘    └─────┬──────┘             │
│        │                 │                 │                     │
│        │ 1. Initiate     │                 │                     │
│        │    verification │                 │                     │
│        ↓                 │                 │                     │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                    Aurora Backend                        │    │
│  │  - User database                                         │    │
│  │  - Verification API                                      │    │
│  └─────────────────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────────────────┘
         │                                    │
         │ 2. Call verification API           │ 7. View dashboard
         │                                    │
         ↓                                    ↓
┌──────────────────────────────────────────────────────────────────┐
│                              Sash                                 │
│  ┌────────────┐    ┌────────────┐    ┌────────────┐             │
│  │  Streamlit │    │   API      │    │ Domain     │             │
│  │     UI     │    │   Layer    │    │   Core     │             │
│  │  (demo)    │    │ (future)   │    │            │             │
│  └────────────┘    └────────────┘    └─────┬──────┘             │
│                                            │                     │
│                                      ┌─────┴──────┐             │
│                                      │ Persistence│             │
│                                      │  (SQLite)  │             │
│                                      └────────────┘             │
└──────────────────────────────────────────────────────────────────┘
         │
         │ 3. Send verification
         │ 4. Receive delivery events
         │
         ↓
┌──────────────────────────────────────────────────────────────────┐
│                         Sinch Platform                           │
│  ┌────────────┐    ┌────────────┐    ┌────────────┐             │
│  │ Messaging  │    │ Verification│   │ Conversation│            │
│  │    API     │    │    API      │   │    API      │            │
│  └─────┬──────┘    └─────┬──────┘    └─────┬──────┘             │
│        │                 │                 │                     │
│        └─────────────────┴─────────────────┘                     │
│                          │                                       │
└──────────────────────────┼───────────────────────────────────────┘
                           │
                           │ 5. Route message
                           │ 6. Delivery reports
                           │
                           ↓
                ┌─────────────────────┐
                │  Mobile Network /   │
                │  Email Provider /   │
                │  WhatsApp Business  │
                └─────────────────────┘
```

## Actors

### Aurora Marketplace

- **Role:** Customer integrating Sash for user verification
- **Needs:** Reliable verification, audit trail, operational visibility
- **Interactions:** Calls Sash API, views operations dashboard

### Sash

- **Role:** Verification orchestration and observability layer
- **Needs:** Sinch API integration, state management, event processing
- **Interactions:** Receives verification requests, calls Sinch, persists events, exposes dashboard

### Sinch

- **Role:** Communications provider (SMS, WhatsApp, email, voice)
- **Needs:** API requests, webhook endpoints
- **Interactions:** Sends messages, returns delivery reports

### End User (Alice)

- **Role:** Aurora Marketplace user being verified
- **Needs:** Quick, frictionless verification
- **Interactions:** Receives messages, submits codes

## Trust boundaries

1. **Aurora → Sash:** API authentication required
2. **Sash → Sinch:** API key authentication
3. **Sinch → Sash:** Webhook signature validation
4. **Sash → Persistence:** Data protection at rest
5. **User → Aurora:** Input validation, consent capture

## External dependencies

- Sinch APIs (Messaging, Verification, Conversation)
- Mobile networks (SMS delivery)
- Email providers (SMTP)
- WhatsApp Business API

## References

- Sinch API documentation: https://developers.sinch.com
- Sash README: ../../README.md
