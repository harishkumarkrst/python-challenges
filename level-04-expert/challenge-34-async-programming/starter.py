import asyncio


async def async_greet(name, delay=0):
    """
    Wait for delay seconds and return greeting.
    """

    await asyncio.sleep(delay)

    return f"Hello, {name}!"


async def fetch_multiple(names, delay=0):
    """
    Fetch all greetings concurrently.
    """

    coroutines = [async_greet(name, delay) for name in names]

    results = await asyncio.gather(*coroutines)

    return list(results)


async def async_countdown(start):
    """
    Async generator countdown.
    """

    for i in range(start, 0, -1):
        await asyncio.sleep(0)
        yield i


async def run_with_timeout(coro, timeout):
    """
    Run coroutine with timeout limit.
    """

    try:
        return await asyncio.wait_for(coro, timeout=timeout)

    except asyncio.TimeoutError:
        return None