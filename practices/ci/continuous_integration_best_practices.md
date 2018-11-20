# Best Practices | CI-CD

## Best Practices

https://en.wikipedia.org/wiki/Continuous_integration#Best_practices

### Maintain a code repository

### Automate the build

### Make the build self-testing

### Everyone commits to the baseline every day

### Every commit (to baseline) should be built

### Keep the build fast

### Test in a clone of the production environment

### Make it easy to get the latest deliverables

### Everyone can see the results of the latest build

### Automate deployment

## Notes

 * Beware large monolithic projects. The bigger they get, the more tests there are, and the harder it is to have a successful build as different parts of it constantly change. Segment your project or split it off if it's getting too difficult to keep the builds clean.

 * Use Multi-stage Continuous Integration to better manage large projects. https://en.wikipedia.org/wiki/Multi-stage_continuous_integration
