from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()

def schedule_recurring_task(task: Task):
    if task.recurrence_rule == "daily":
        scheduler.add_job(
            create_next_task,
            'interval',
            days=1,
            args=[task],
            id=f"task_{task.id}"
        )
    # Аналогично для weekly/monthly

def create_next_task(task: Task):
    new_task = Task(
        title=task.title,
        category=task.category,
        deadline=task.deadline + timedelta(days=1),
        priority=task.priority,
        is_recurring=True,
        recurrence_rule=task.recurrence_rule
    )
    session.add(new_task)
    session.commit()
