# Tasks

## List task lists

```bash
gog tasks lists [--max N] [--page TOKEN]
```

## Create task list

```bash
gog tasks lists create <title>
```

## List tasks in a list

```bash
gog tasks list <tasklistId> [--max N] [--page TOKEN]
```

## Get a task

```bash
gog tasks get <tasklistId> <taskId>
```

## Add a task

```bash
gog tasks add <tasklistId> --title T [--notes N] \
  [--due RFC3339|YYYY-MM-DD] \
  [--repeat daily|weekly|monthly|yearly] [--repeat-count N] [--repeat-until DT] \
  [--parent ID] [--previous ID]
```

- `--parent`: create as subtask
- `--previous`: insert after this task
- `--repeat`: create recurring task

## Update a task

```bash
gog tasks update <tasklistId> <taskId> [--title T] [--notes N] \
  [--due RFC3339|YYYY-MM-DD] [--status needsAction|completed]
```

## Mark as done

```bash
gog tasks done <tasklistId> <taskId>
```

## Mark as not done

```bash
gog tasks undo <tasklistId> <taskId>
```

## Delete a task

```bash
gog tasks delete <tasklistId> <taskId>
```

## Clear completed tasks

```bash
gog tasks clear <tasklistId>
```

Removes all completed tasks from a list.
