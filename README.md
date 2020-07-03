# zendesk-api-trash
Simple, semi-automated code to remove the trash from Zendesk
100 tickets at a time (that's the max their /api/v2/deleted_tickets module accepts)

# How it works
You run this within a Linux environment, run the script through 'watch' and leave a lot of time because Zendesk is incredibly slow.

# EXAMPLE
'watch -n 600 python3 main.py &'

- The reason is that Zendesk takes FOREVER to remove bulk tickets so this may create 404s and competing requests that fail.
- Running this every 10 min. (-n 600) its easier than setting the loop in Python and checking the job status, etc. Too much unnecessary code.
- Turn this on and leave on background. Code can be better and stop with 3-5 404s in a row, but easier just turn it off at some point.
