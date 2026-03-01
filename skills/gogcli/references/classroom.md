# Classroom

## Courses

```bash
gog classroom courses [--state ACTIVE|ARCHIVED|...] [--max N] [--page TOKEN]
gog classroom courses get <courseId>
gog classroom courses create --name NAME [--owner me] [--state ACTIVE|...]
gog classroom courses update <courseId> [--name ...] [--state ...]
gog classroom courses delete <courseId>
gog classroom courses archive <courseId>
gog classroom courses unarchive <courseId>
gog classroom courses join <courseId> [--role student|teacher] [--user me]
gog classroom courses leave <courseId> [--role student|teacher] [--user me]
gog classroom courses url <courseId...>
```

## Students

```bash
gog classroom students <courseId> [--max N] [--page TOKEN]
gog classroom students get <courseId> <userId>
gog classroom students add <courseId> <userId> [--enrollment-code CODE]
gog classroom students remove <courseId> <userId>
```

## Teachers

```bash
gog classroom teachers <courseId> [--max N] [--page TOKEN]
gog classroom teachers get <courseId> <userId>
gog classroom teachers add <courseId> <userId>
gog classroom teachers remove <courseId> <userId>
```

## Roster (students + teachers)

```bash
gog classroom roster <courseId> [--students] [--teachers]
```

## Coursework

```bash
gog classroom coursework <courseId> [--state ...] [--topic TOPIC_ID] [--scan-pages N] [--max N] [--page TOKEN]
gog classroom coursework get <courseId> <courseworkId>
gog classroom coursework create <courseId> --title TITLE [--type ASSIGNMENT|...]
gog classroom coursework update <courseId> <courseworkId> [--title ...]
gog classroom coursework delete <courseId> <courseworkId>
gog classroom coursework assignees <courseId> <courseworkId> [--mode ...] [--add-student ...]
```

## Materials

```bash
gog classroom materials <courseId> [--state ...] [--topic TOPIC_ID] [--scan-pages N] [--max N] [--page TOKEN]
gog classroom materials get <courseId> <materialId>
gog classroom materials create <courseId> --title TITLE
gog classroom materials update <courseId> <materialId> [--title ...]
gog classroom materials delete <courseId> <materialId>
```

## Submissions

```bash
gog classroom submissions <courseId> <courseworkId> [--state ...] [--max N] [--page TOKEN]
gog classroom submissions get <courseId> <courseworkId> <submissionId>
gog classroom submissions turn-in <courseId> <courseworkId> <submissionId>
gog classroom submissions reclaim <courseId> <courseworkId> <submissionId>
gog classroom submissions return <courseId> <courseworkId> <submissionId>
gog classroom submissions grade <courseId> <courseworkId> <submissionId> [--draft N] [--assigned N]
```

## Announcements

```bash
gog classroom announcements <courseId> [--state ...] [--max N] [--page TOKEN]
gog classroom announcements get <courseId> <announcementId>
gog classroom announcements create <courseId> --text TEXT
gog classroom announcements update <courseId> <announcementId> [--text ...]
gog classroom announcements delete <courseId> <announcementId>
gog classroom announcements assignees <courseId> <announcementId> [--mode ...]
```

## Topics

```bash
gog classroom topics <courseId> [--max N] [--page TOKEN]
gog classroom topics get <courseId> <topicId>
gog classroom topics create <courseId> --name NAME
gog classroom topics update <courseId> <topicId> --name NAME
gog classroom topics delete <courseId> <topicId>
```

## Invitations

```bash
gog classroom invitations [--course ID] [--user ID]
gog classroom invitations get <invitationId>
gog classroom invitations create <courseId> <userId> --role STUDENT|TEACHER|OWNER
gog classroom invitations accept <invitationId>
gog classroom invitations delete <invitationId>
```

## Guardians

```bash
gog classroom guardians <studentId> [--max N] [--page TOKEN]
gog classroom guardians get <studentId> <guardianId>
gog classroom guardians delete <studentId> <guardianId>
gog classroom guardian-invitations <studentId> [--state ...] [--max N] [--page TOKEN]
gog classroom guardian-invitations get <studentId> <invitationId>
gog classroom guardian-invitations create <studentId> --email EMAIL
```

## Profile

```bash
gog classroom profile [userId]
```
