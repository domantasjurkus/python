#!/usr/bin/env ruby

require 'chunky_png'

image = ChunkyPNG::Image.from_file('blue.png')

answer = []

(0...image.dimension.height).each { |y|
  msg = ''
  (0...image.dimension.width).each { |x|
    msg += ChunkyPNG::Color.b(image[x,y]).chr
  }
  answer << msg
}

answer.reverse_each { |a| puts a }