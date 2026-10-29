-- Execute in Supabase SQL Editor. Keep RLS enabled.
create table if not exists public.learner_progress (
 user_id uuid primary key references auth.users(id) on delete cascade,
 progress jsonb not null default '{}'::jsonb,
 updated_at timestamptz not null default now()
);
alter table public.learner_progress enable row level security;
revoke all on public.learner_progress from anon;
grant select, insert, update, delete on public.learner_progress to authenticated;
drop policy if exists "Learners read their own progress" on public.learner_progress;
create policy "Learners read their own progress" on public.learner_progress for select to authenticated using ((select auth.uid())=user_id);
drop policy if exists "Learners create their own progress" on public.learner_progress;
create policy "Learners create their own progress" on public.learner_progress for insert to authenticated with check ((select auth.uid())=user_id);
drop policy if exists "Learners update their own progress" on public.learner_progress;
create policy "Learners update their own progress" on public.learner_progress for update to authenticated using ((select auth.uid())=user_id) with check ((select auth.uid())=user_id);
drop policy if exists "Learners delete their own progress" on public.learner_progress;
create policy "Learners delete their own progress" on public.learner_progress for delete to authenticated using ((select auth.uid())=user_id);
