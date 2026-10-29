# Parlance French — Version 3

Mobile-app-like installable PWA. First-visit learner onboarding asks whether the learner **already has an official** CEFR proficiency result; this is **self-reported and unverified**, not an official rating issued by Parlance. Unrated users can start at beginner, then take the optional adaptive indicative check.

## Deploy and activate secure accounts

1. Create a Supabase project. In Supabase **SQL Editor**, run `supabase-schema.sql` to create learner progress table and ownership-based row-level security (RLS).
2. Under **Authentication → Providers → Email**, enable email/password; enable email confirmation. Under Authentication → URL Configuration set Site URL to your Vercel URL and add your Vercel URL to redirect allowlist. Configure email delivery appropriately for public production use.
3. In `config.js` insert your **Project URL** and **publishable/anon public API key** (not service_role, not secret). These values are safe to ship client-side because RLS protects learner data. Never put private service keys in browser files.
4. Upload these files to your GitHub repository root (not inside an extra folder). Deploy with Vercel framework **Other**, no build command. HTTPS is provided by Vercel. Sign up, confirm email and test sign-in/sync using two devices.
5. Add your own privacy policy, terms, support contacts and account-deletion workflow before public launch; confirm legal requirements for target regions. Set custom SMTP for reliable transactional email.

Without a configured backend the app remains usable in guest mode, but **cloud sign-in is inactive**. Browser storage holds guest progress; export/import works offline. Cloud sync is online-only, last-write-wins per account; avoid simultaneous offline edits on multiple devices. On first successful account sign-in, if no existing cloud progress, local guest progress is uploaded. When cloud progress exists, it replaces local state to prevent accidental mixing of profiles. On sign out, cached local progress is cleared from the active app.

## Product limits

56 introductory/guided topic modules, placement knowledge screen and optional listening tasks are **not a validated complete CEFR course or proficiency certification**. Google Translate links are external and require a separate click on Google's speaker; some IPA remains unverified. Google speaker availability is controlled by Google. Device voice is optional and may not be available. No actual MP3 archive is provided.

## PWA

The mobile layout uses a fixed bottom navigation, safe-area support, full-height app shell and installable web manifest. For installation open the deployed URL and use the browser's Add to Home Screen / Install App action. Test PWA installation and touch interactions on representative iOS and Android devices.
